import requests
from bs4 import BeautifulSoup


def extract_song_info(song_url: str) -> tuple[None, None] | tuple[str, str]:
    """
    Extracts the song title and artist from a given song URL.

    This function makes a HTTP request to the provided song URL and parses the HTML content
    to find the title and artist information. The function expects the title to contain a
    specific format ('<title> - song by <artist>') separated by a '|'. If the format is not
    found or an error occurs, it returns None for both values.

    Parameters
    ----------
    song_url : str
        The URL of the song to extract information from.

    Returns
    -------
    tuple[None, None] | tuple[str, str]
        A tuple containing the title and artist of the song. If the information cannot be
        extracted, both elements of the tuple are None.
    """

    try:
        response = requests.get(song_url)
        # print(response.text)
        soup = BeautifulSoup(response.text, "html.parser")
        title_tag = soup.title.string

        if "|" in title_tag:
            title, artist = title_tag.split("|")[0].strip().split(" - song by ")
            title, artist = title.strip(), artist.strip()
            return title, artist
        else:
            return None, None

    except Exception as e:
        print(f"Error processing URL {song_url}: {e}")
        return None, None


def extract_from_txt() -> list[str]:
    """
    Reads song URLs from a text file and extracts song information.

    This function reads URLs from a file named 'playlist-urls.txt', then uses the
    `extract_song_info` function to extract the song title and artist for each URL.
    If the information is successfully extracted, it is formatted as '<song_name> - <artist_name>'
    and added to the list. If extraction fails, a message is printed.

    Returns
    -------
    list[str]
        A list of strings, each containing the song title and artist formatted as
        '<song_name> - <artist_name>'. If extraction fails for any URL, that URL is skipped.
    """

    file_path = "playlist-urls.txt"

    with open(file_path, "r") as file:
        urls = file.readlines()

    urls = [url.strip() for url in urls]

    song_infos = []
    for url in urls:
        if url:
            song_name, artist_name = extract_song_info(url)
            if song_name and artist_name:
                song_info = f"{song_name} - {artist_name}"
                song_infos.append(song_info)
            else:
                print(f"Could not extract information from URL: {url}")

    return song_infos
