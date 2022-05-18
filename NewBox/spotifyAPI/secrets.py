import os

SPOTIFY_CLIENT_ID = os.environ.get('spotify_client_id')
SPOTIFY_CLIENT_SECRET = os.environ.get('spotify_client_secret')
SPOTIFY_REDIRECT_URI = 'http://localhost:8080'
USER = '31dpnolbrnlodprs3cph3m5izary'
SCOPES = ["user-modify-playback-state",
          "user-read-playback-state",
          "user-read-currently-playing",
          "user-follow-modify",
          "user-follow-read",
          "user-read-recently-played",
          "user-read-playback-position",
          "user-top-read",
          "playlist-read-collaborative",
          "playlist-modify-public",
          "playlist-read-private",
          "playlist-modify-private",
          "user-read-email",
          "user-read-private",
          "user-library-modify",
          "user-library-read",
          "app-remote-control",
          "streaming"]
