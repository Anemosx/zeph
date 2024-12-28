# Zeph - Spotify Playlist Extractor

![MIT license](https://img.shields.io/badge/license-MIT-blue)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Black Linting](https://github.com/Anemosx/zeph/actions/workflows/lint.yml/badge.svg)](https://github.com/Anemosx/zeph/actions/workflows/lint.yml)
[![PyTest](https://github.com/Anemosx/zeph/actions/workflows/test.yml/badge.svg)](https://github.com/Anemosx/zeph/actions/workflows/test.yml)

Zeph is a user-friendly tool designed to make extracting Spotify playlists effortless.
With Zeph, you can easily retrieve the songs from any Spotify playlist by simply
pasting its URL. Once the URL is provided, the tool quickly processes the playlist,
extracting all the tracks and presenting them in a neatly organized table.
Whether you’re curating music, analyzing playlists, or just saving your favorite songs,
Zeph streamlines the process, saving you time and effort.


## Installation

**Install Project Dependencies**
To get started, ensure you have Poetry installed to manage project dependencies.
Follow these steps:
1. Install Poetry:
   ```bash
   pip install poetry
   ```

2. Install the project dependencies:
   ```bash
   poetry install
   ```

## Running the Project

### 1. Running the Backend Server

Launch the backend server by executing the following command:

```bash
python app/main.py
```

### 2. Accessing the Frontend

With the server running, open your web browser and navigate to:

[http://localhost:8000](http://localhost:8000)

![zeph_input](docs/zeph_input.png)

Follow the instructions on the page to extract your Spotify playlists.

![zeph_output](docs/zeph_output.png)

Enjoy your music!
