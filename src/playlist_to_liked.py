import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.environ["SPOTIPY_CLIENT_ID"],
    client_secret=os.environ["SPOTIPY_CLIENT_SECRET"],
    redirect_uri="http://127.0.0.1:8888/callback",
    scope="playlist-read-private playlist-read-collaborative "
          "user-library-read user-library-modify",
))

def paginate(page):
    while page:
        yield from page["items"]
        page = sp.next(page) if page["next"] else None

# Bereits geliked
liked = {i["track"]["id"] for i in paginate(sp.current_user_saved_tracks(limit=50))}

# Alle Tracks aus allen Playlists
new = set()
for pl in paginate(sp.current_user_playlists(limit=50)):
    for item in paginate(sp.playlist_items(pl["id"], limit=100)):
        t = item.get("track")
        if t and t.get("id") and not t.get("is_local"):
            new.add(t["id"])

to_add = list(new - liked)
print(f"{len(to_add)} neue Songs")

for i in range(0, len(to_add), 50):
    sp.current_user_saved_tracks_add(to_add[i:i+50])