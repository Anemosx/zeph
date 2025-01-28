from app.extract.songs import extract_song_info


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

    song_data = []
    for i, song_url in enumerate(song_urls):
        title, artist = extract_song_info(song_url, access_token)
        if title is not None and artist is not None:
            song_data.append({"url": song_url, "title": title, "artist": artist})
            if verbose:
                separator = "," if i < len(song_urls) - 1 else "\n"
                print(f"{title} - {artist}{separator}")
        else:
            song_data.append({"url": song_url, "title": "unknown", "artist": "unknown"})

    return song_data
