import os

# spotify_client_id and spotify_client_secret must be set as environment variables on own pc
# these can be found by logging in to developer.spotify.com -> dashboard -> copy codes and add them as envs
SPOTIFY_CLIENT_ID = 'a23ef867ab284c908c1a11e3bc0b5de3'
SPOTIFY_CLIENT_SECRET = '82b88bcc5a384fb1aca691ef256b3d6f'
SPOTIFY_REDIRECT_URI = 'http://localhost:8080'
DEVICE_ID = '79b46bb2d19459b85244fa3b1731f5c6545d3b0b'
USER = '130367-nl'
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
