from app.extract.songs import extract_song_info


def extract_playlist_info(song_urls: list[str]) -> list[dict[str, str]]:
    """
    Extracts song information from a list of song URLs.

    This function takes a list of song URLs and extracts the title and artist for each song
    using the `extract_song_info` function. If the title or artist cannot be determined,
    it defaults to "unknown".

    Parameters
    ----------
    song_urls : list[str]
        A list of URLs pointing to individual songs.

    Returns
    -------
    song_data : list[dict[str, str]]
        A list of dictionaries, each containing the URL of the song (`'url'`),
        the title of the song (`'title'`), and the artist of the song (`'artist'`).
        If the title or artist is not found, they are set to "unknown".
    """

    song_data = []
    for song_url in song_urls:
        title, artist = extract_song_info(song_url)
        if title is not None and artist is not None:
            song_data.append({"url": song_url, "title": title, "artist": artist})
        else:
            song_data.append({"url": song_url, "title": "unknown", "artist": "unknown"})

    return song_data
