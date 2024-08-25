from app.extract import extract_song_info


def test_extract_song_info_valid(mock_valid_song_page, valid_song_url: str) -> None:
    title, artist = extract_song_info(valid_song_url)

    assert title == "Never Gonna Give You Up"
    assert artist == "Rick Astley"


def test_extract_song_info_invalid_format(
    mock_invalid_format_page, invalid_format_url: str
) -> None:
    title, artist = extract_song_info(invalid_format_url)

    assert title is None
    assert artist is None


def test_extract_song_info_network_error(
    mock_network_error, network_error_url: str
) -> None:
    title, artist = extract_song_info(network_error_url)

    assert title is None
    assert artist is None


def test_extract_song_info_no_title_tag(
    mock_no_title_tag_page, no_title_tag_url: str
) -> None:
    title, artist = extract_song_info(no_title_tag_url)

    assert title is None
    assert artist is None
