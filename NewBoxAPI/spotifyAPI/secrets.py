import os

# spotify_client_id and spotify_client_secret must be set as environment variables on own pc
# these can be found by logging in to developer.spotify.com -> dashboard -> copy codes and add them as envs
# SPOTIFY_CLIENT_ID = os.environ.get('spotify_client_id')
# SPOTIFY_CLIENT_SECRET = os.environ.get('spotify_client_secret')
SPOTIFY_REDIRECT_URI = 'http://localhost:8080'
DEVICE_ID = '79b46bb2d19459b85244fa3b1731f5c6545d3b0b'
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
