import base64
import os

import requests


def get_spotify_token(
    client_id: str | None = None, client_secret: str | None = None
) -> str | None:
    """
    Get a new Spotify access token using client credentials.

    Parameters
    ----------
    client_id : str | None, optional
        The Spotify client ID. If None, reads from environment variable.
    client_secret : str | None, optional
        The Spotify client secret. If None, reads from environment variable.

    Returns
    -------
    str | None
        The access token if successful, None otherwise.
    """
    try:
        client_id = client_id or os.getenv("SPOTIFY_CLIENT_ID")
        client_secret = client_secret or os.getenv("SPOTIFY_CLIENT_SECRET")

        if not (client_id and client_secret):
            return None

        auth = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
        headers = {
            "Authorization": f"Basic {auth}",
            "Content-Type": "application/x-www-form-urlencoded",
        }
        data = {"grant_type": "client_credentials"}

        response = requests.post(
            "https://accounts.spotify.com/api/token", headers=headers, data=data
        )
        response.raise_for_status()
        return response.json()["access_token"]

    except Exception as e:
        return None
