from pathlib import Path

from fastapi import APIRouter, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from starlette.responses import JSONResponse

from app.extract.playlists import extract_playlist_info

router = APIRouter()

extract_html_file_path = Path("static") / "extract" / "index.html"
with extract_html_file_path.open("r") as file:
    extract_content = file.read()


class URLRequest(BaseModel):
    urls: list[str]


@router.get("/", response_class=HTMLResponse)
async def read_root() -> HTMLResponse:
    """
    Returns the HTML content of the root page.

    This function reads the HTML content from a pre-defined file and returns it
    as an HTML response. The response includes a header to disable caching.

    Returns
    -------
    HTMLResponse
        An HTML response containing the content of the root page.
    """

    response = HTMLResponse(content=extract_content)
    response.headers["Cache-Control"] = "public, max-age=0"

    return response


@router.post("/submit_song_urls")
async def submit_urls(url_request: URLRequest) -> JSONResponse:
    """
    Processes a list of song URLs and returns the extracted song information.

    This function receives a POST request containing a list of song URLs, validates the input,
    and extracts song information using the `extract_playlist_info` function. If no URLs are
    provided, it raises an HTTP 400 error.

    Parameters
    ----------
    url_request : URLRequest
        A Pydantic model containing a list of song URLs.

    Returns
    -------
    JSONResponse
        A JSON response containing the extracted song information in the format:
        `{"songs": [{"url": "song_url", "title": "song_title", "artist": "song_artist"}, ...]}`.
    """

    urls = url_request.urls
    if not urls:
        raise HTTPException(status_code=400, detail="No URLs provided")

    song_data = extract_playlist_info(urls)

    return JSONResponse({"songs": song_data})
