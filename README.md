# playlist-to-liked

A small Python script that adds every song from your Spotify playlists to your **Liked Songs**. Songs you have already liked are skipped.

## Features

- Reads all of your own playlists
- Removes duplicates and songs that are already liked
- Adds new songs in batches of 40
- Automatically skips local files and podcast episodes

## Requirements

- Python 3.9+
- A Spotify account
- An app of your own in the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard)

## Installation

```bash
git clone git@github.com:mphcamara/playlist-to-liked.git
cd playlist-to-liked
pip install -r requirements.txt
```

`requirements.txt`:

```
spotipy
```

## Setup

1. In the Developer Dashboard, click **Create app**.
2. Set the **Redirect URI** to `http://127.0.0.1:8888/callback` and select **Web API**.
3. Under **Settings**, copy the **Client ID** and the **Client secret**.
4. Set both as environment variables:

```bash
# Linux/macOS
export SPOTIPY_CLIENT_ID="your_client_id"
export SPOTIPY_CLIENT_SECRET="your_client_secret"

# Windows (PowerShell)
$env:SPOTIPY_CLIENT_ID="your_client_id"
$env:SPOTIPY_CLIENT_SECRET="your_client_secret"
```

## Usage

```bash
python playlist_to_liked.py
```

On the first run, a browser window opens for Spotify login. After you confirm, the script runs and prints how many new songs were added.

## Notes

- **Date added:** Newly added songs get today's date as their "added at" date. Their order within a batch may vary, so don't rely on it.
- **Followed playlists:** By default, playlists you only follow (e.g. Spotify mixes) are included as well. To restrict the script to your own playlists, filter with `pl["owner"]["id"] == sp.me()["id"]`.
- **Not easily undone:** The script never removes anything, but a bulk import can only be cleaned up manually afterwards. Consider backing up your Liked Songs first.
- **API changes:** Spotify occasionally changes its Web API. If you run into errors, try `pip install -U spotipy` first.

## Security

- **Never** commit or share your client secret.
- Spotipy stores a token file named `.cache` in the project folder. Add it to your `.gitignore`:

```
.cache
```

## License

MIT. See [LICENSE](LICENSE).
