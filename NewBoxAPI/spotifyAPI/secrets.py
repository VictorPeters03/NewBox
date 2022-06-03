import os

# spotify_client_id and spotify_client_secret must be set as environment variables on own pc
# these can be found by logging in to developer.spotify.com -> dashboard -> copy codes and add them as envs
SPOTIFY_CLIENT_ID = '99117380ca794cdeadaa05089d88c79d'
SPOTIFY_CLIENT_SECRET = 'f6d7ae770020431ab0b8a9190822d41f'
SPOTIFY_REDIRECT_URI = 'http://localhost:8080'
DEVICE_ID = '9a8e38100faa637635ff6e5402aec481ca3f2772'
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
