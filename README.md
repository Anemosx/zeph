# Zeph - Spotify Playlist Extractor

![MIT license](https://img.shields.io/badge/license-MIT-blue)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[![Black Linting](https://github.com/Anemosx/zeph/actions/workflows/lint.yml/badge.svg)](https://github.com/Anemosx/zeph/actions/workflows/lint.yml)
[![PyTest](https://github.com/Anemosx/zeph/actions/workflows/test.yml/badge.svg)](https://github.com/Anemosx/zeph/actions/workflows/test.yml)

Zeph is a user-friendly tool designed to make extracting Spotify playlists effortless.
With Zeph, you can easily retrieve the songs from any Spotify playlist by simply
pasting its URL. Once the URL is provided, the tool quickly processes the playlist,
extracting all the tracks and presenting them in a neatly organized table.
Whether you're curating music, analyzing playlists, or just saving your favorite songs,
Zeph streamlines the process, saving you time and effort.


## Installation

### 1. Using Poetry

This section guides you through setting up Zeph using Poetry, a modern Python dependency management tool.

#### Prerequisites
- Python 3.11 or higher
- pip (Python package installer)

#### Setup Steps

1. Install Poetry if you haven't already:
   ```bash
   pip install poetry
   ```

2. Clone the repository and install dependencies:
   ```bash
   git clone https://github.com/Anemosx/zeph.git
   cd zeph
   poetry install
   ```

3. Configure Environment Variables (Optional)
   Create a `.env` file in the project root with the following options:

   ```ini
   # Spotify API Credentials (from https://developer.spotify.com/dashboard)
   SPOTIFY_CLIENT_ID=your_client_id_here
   SPOTIFY_CLIENT_SECRET=your_client_secret_here

   # Enable detailed logging (optional)
   VERBOSE=True
   ```

## Running Zeph

### Starting the Application

1. Launch the server:
   ```bash
   poetry run python app/main.py
   ```

2. Access the web interface:
   Open your browser and visit [http://localhost:8088](http://localhost:8088)

The application will now be ready to extract your Spotify playlists.


### 2. Using Docker

This section guides you through setting up Zeph using Docker, a containerization platform that ensures consistent environments across different systems.

#### Prerequisites
- Docker and Docker Compose installed on your system

#### Setup Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/Anemosx/zeph.git
   cd zeph
   ```

2. Configure Environment Variables
   Create a `.env` file in the project root with your credentials:
   ```ini
   # Spotify API Credentials (from https://developer.spotify.com/dashboard)
   SPOTIFY_CLIENT_ID=your_client_id_here
   SPOTIFY_CLIENT_SECRET=your_client_secret_here

   # Enable detailed logging (optional)
   VERBOSE=True
   ```

#### Running the Application

1. Start the container using Docker Compose:
   ```bash
   docker compose up
   ```
   Or to run in detached mode:
   ```bash
   docker compose up -d
   ```

2. Access the web interface:
   Open your browser and visit [http://localhost:8088](http://localhost:8088)

The application will now be ready to extract your Spotify playlists.

## Usage

![zeph_input](docs/zeph_input.png)

Follow the instructions on the page to extract your Spotify playlists.

![zeph_output](docs/zeph_output.png)

Enjoy your music!
