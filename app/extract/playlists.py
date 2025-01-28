from concurrent.futures import ThreadPoolExecutor
import time
from app.extract.songs import extract_song_info


def process_url(
    args: tuple[int, str], access_token: str | None = None
) -> tuple[int, dict[str, str]]:
    """
    Process a single Spotify URL to extract song metadata.

    Parameters
    ----------
    args : tuple[int, str]
        Tuple containing index and Spotify song URL.
    access_token : str | None, optional
        Spotify API access token for authentication. Defaults to None.

    Returns
    -------
    tuple[int, dict[str, str]]
        Tuple containing original index and song metadata dictionary.
    """
    i, song_url = args

    # respect spotify rate limit
    time.sleep(0.3)
    title, artist = extract_song_info(song_url, access_token)

    if title is not None and artist is not None:
        return i, {"url": song_url, "title": title, "artist": artist}

    return i, {"url": song_url, "title": "unknown", "artist": "unknown"}


def extract_playlist_info(
    song_urls: list[str], access_token: str | None = None, verbose: bool = False
) -> list[dict[str, str]]:
    """
    Extract metadata from a list of Spotify song URLs.

    Parameters
    ----------
    song_urls : list[str]
        List of Spotify song URLs to process.
    access_token : str | None, optional
        Spotify API access token for authentication. Defaults to None.
    verbose : bool, optional
        Whether to print song info as they are processed. Defaults to False.

    Returns
    -------
    list[dict[str, str]]
        List of dictionaries containing song metadata:
            - url : str
                Original Spotify URL
            - title : str
                Song title, or "unknown" if extraction failed
            - artist : str
                Artist name, or "unknown" if extraction failed
    """

    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(
            executor.map(
                lambda args: process_url(args, access_token), enumerate(song_urls)
            )
        )
        song_data = [data for _, data in sorted(results, key=lambda x: x[0])]

    if verbose:
        for i, song in enumerate(song_data):
            separator = "," if i < len(song_data) - 1 else "\n"
            if song["title"] != "unknown":
                print(f"{song['title']} - {song['artist']}{separator}")

    return song_data
