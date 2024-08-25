from pathlib import Path
from typing import Generator

import pytest
import json
from unittest.mock import patch, MagicMock
from requests.exceptions import RequestException


@pytest.fixture(scope="session")
def load_json_content() -> dict[str, any]:
    current_dir = Path(__file__).parent
    json_path = current_dir / "test.json"
    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


@pytest.fixture
def valid_song_url() -> str:
    return "https://open.spotify.com/track/4PTG3Z6ehGkBFwjybzWkR8"


@pytest.fixture
def invalid_format_url() -> str:
    return "https://open.spotify.com/track/xxx"


@pytest.fixture
def no_title_tag_url() -> str:
    return "https://open.spotify.com/track/4PTG3Z6ehGkBFwjybzWkR8xx"


@pytest.fixture
def network_error_url() -> str:
    return "http://network-error-url.com"


@pytest.fixture
def mock_requests_get() -> Generator[MagicMock, None, None]:
    with patch("requests.get") as mock_get:
        yield mock_get


@pytest.fixture
def mock_valid_song_page(
    mock_requests_get: MagicMock, load_json_content: dict[str, any]
) -> None:
    content = load_json_content["valid_song_page"]
    mock_requests_get.return_value.text = content


@pytest.fixture
def mock_invalid_format_page(
    mock_requests_get: MagicMock, load_json_content: dict[str, any]
) -> None:
    content = load_json_content["invalid_format_page"]
    mock_requests_get.return_value.text = content


@pytest.fixture
def mock_no_title_tag_page(
    mock_requests_get: MagicMock, load_json_content: dict[str, any]
) -> None:
    content = load_json_content["no_title_tag_page"]
    mock_requests_get.return_value.text = content


@pytest.fixture
def mock_network_error(mock_requests_get: MagicMock) -> None:
    mock_requests_get.side_effect = RequestException("Network error")
