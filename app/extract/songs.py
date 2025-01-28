import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from app.utils.spotify import get_spotify_token


def extract_song_info(
    song_url: str, access_token: str | None = None
) -> tuple[None, None] | tuple[str, str]:
    """
    Extract song title and artist from a Spotify song URL.

    Parameters
    ----------
    song_url : str
        Spotify song URL to extract information from.
    access_token : str | None, optional
        Spotify API access token. If provided, attempts API call first.
        Defaults to None.

    Returns
    -------
    tuple[None, None] | tuple[str, str]
        Song title and artist name if successful, (None, None) if extraction fails.
    """

    if access_token:
        try:
            track_id = song_url.split("/")[-1].split("?")[0]
            api_url = urljoin("https://api.spotify.com/v1/tracks/", track_id)
            headers = {"Authorization": f"Bearer {access_token}"}

            response = requests.get(api_url, headers=headers)
            response.raise_for_status()
            track_info = response.json()

            title = track_info["name"]
            artist = track_info["artists"][0]["name"]
            return title, artist

        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                new_token = get_spotify_token()
                if new_token:
                    return extract_song_info(song_url, new_token)
            print(f"Error using Spotify API for URL {song_url}: {e}")
        except Exception as e:
            print(f"Error using Spotify API for URL {song_url}: {e}")

    try:
        response = requests.get(song_url)
        soup = BeautifulSoup(response.text, "html.parser")
        title_tag = soup.title.string

        if "|" in title_tag:
            title, artist = title_tag.split("|")[0].strip().split(" - song by ")
            return title.strip(), artist.strip()

        return None, None

    except Exception as e:
        print(f"Error processing URL {song_url}: {e}")
        return None, None


def extract_from_txt(access_token: str | None = None) -> list[str]:
    """
    Extract song information from URLs stored in a text file.

    Parameters
    ----------
    access_token : str | None, optional
        Spotify API access token. Defaults to None.

    Returns
    -------
    list[str]
        List of formatted strings containing song information.
        Each string follows the format '<song_name> - <artist_name>'.

    Notes
    -----
    Reads URLs from 'playlist-urls.txt' file. Skips URLs where information
    extraction fails and prints error message.
    """

    file_path = "playlist-urls.txt"

    with open(file_path, "r") as file:
        urls = file.readlines()

    urls = [url.strip() for url in urls]

    song_infos = []
    for url in urls:
        if url:
            song_name, artist_name = extract_song_info(url, access_token)
            if song_name and artist_name:
                song_info = f"{song_name} - {artist_name}"
                song_infos.append(song_info)
            else:
                print(f"Could not extract information from URL: {url}")

    return song_infos
