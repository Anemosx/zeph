import os
from pathlib import Path

from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from starlette.responses import JSONResponse

from app.extract.playlists import extract_playlist_info
from app.utils.spotify import get_spotify_token

router = APIRouter()
router.access_token = get_spotify_token()
router.verbose = os.getenv("VERBOSE", False)

extract_html_file_path = Path("static") / "extract" / "index.html"
with extract_html_file_path.open("r") as file:
    extract_content = file.read()


def spotify_token_dependency() -> str:
    return router.access_token


class URLRequest(BaseModel):
    urls: list[str]


@router.get("/", response_class=HTMLResponse)
async def read_root() -> HTMLResponse:
    """
    Serve the main page HTML.

    Returns
    -------
    HTMLResponse
        HTML content with cache disabled.
    """

    response = HTMLResponse(content=extract_content)
    response.headers["Cache-Control"] = "public, max-age=0"

    return response


@router.post("/submit_song_urls")
async def submit_urls(
    url_request: URLRequest, access_token: str = Depends(spotify_token_dependency)
) -> JSONResponse:
    """
    Process Spotify URLs and extract song details.

    Parameters
    ----------
    url_request : URLRequest
        Request containing list of Spotify URLs.
    access_token : str
        Spotify API token.

    Returns
    -------
    JSONResponse
        Extracted song details including titles and artists.

    Raises
    ------
    HTTPException
        If no URLs provided.
    """

    urls = url_request.urls
    if not urls:
        raise HTTPException(status_code=400, detail="No URLs provided")

    song_data = extract_playlist_info(
        song_urls=urls,
        access_token=access_token,
        verbose=router.verbose,
    )

    return JSONResponse({"songs": song_data})
