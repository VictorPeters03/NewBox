import spotipy
from secrets import SPOTIFY_REDIRECT_URI, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, USER, SCOPES
from spotipy.oauth2 import SpotifyOAuth

spAuth = spotipy.oauth2.SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET,
                                     redirect_uri=SPOTIFY_REDIRECT_URI, scope=SCOPES)

authCode = spAuth.parse_response_code(
    url='http://localhost:8080/?code=AQDgQp6viy8xcG9zPTtH0wHchH2scYQmesH35floL2ddMvXKLp-A7JhwxPw6J2mI0yua_jcIIENqFOQ_cjhi4x3D3pyGLp_t1LgGMJoVD7tf61v5RObG2xiuZJLUzGOpB-IRpIPjC1Dcu-pprTeXJxtXQ6Ah054pqKZ2UsmLLdDjOGMXZ0DrsuUIjoiHX-RXWfvvLS1hljjdyXrWV2wk4thw2-etd8OMvQZGAGfj1VJiaG1pUEYS6bTjpDsrGxdJfTuxDCkmBup-qZc8pdff5Um6ouBP2zY7HLIuLDGnpcHY9t9owBGykebJlo7Df1Xx4M-qU71gLdFbPosJSywpaUdpv5SizkM5NZDp8mtzcoYOs-qqr6b8b9g6R6x05sqK53CVwbeYQ6CCRRQJsebgq6cUET1YQrVT3q9lHgErNiorUCF7u32r-HQ9FEK0rZBlz9_73z9y4kTCsX9SiNpduzahDO9dRAfrh3SSpt5EbIVyzx_5bPetBJSiFadYRgzQHo5ls987sb_THwNyWuDwKwSr9CpQXCF3jIDpl2IIK9OKpAOMMQ-c0QnlwJwITnL8OKiYNFvaX1Z39orYfC0mXY37C9NscKSf_lIWXH1ygn3iB1OzGDnPEgdWV0bkqX0hGWc6-bYr0_SG7jCigGlfg8cfw1Ff-4psiv3rTTbghEkToaos_O-uq9s')

if spAuth.get_cached_token()['access_token'] is None:
    accessData = spAuth.get_access_token(code=authCode, as_dict=True)

token = spAuth.get_cached_token()['access_token']
refreshToken = spAuth.get_cached_token()['refresh_token']
# spAuth.refresh_access_token(refreshToken)

spotifyHandler = spotipy.Spotify(token)


# Expire en scope even toegevoegd om te testen

# def _init_(spAuth):
    #spAuth.spotify_object = token.objects.get(account_provider="Spotify")


# def get_cached_token(spAuth):
    # token_info = {"access_token": spAuth.spotify_object.token, "refresh_token": spAuth.spotify_object.token_secret,
                  # "expires_at": spAuth.spotify_object.expires_at, "scope": spAuth.spotify_object.scope}

    # return token_info


# def save_token_to_cache(spAuth, token_info):
    # spAuth.spotify_object.token = token_info["access_token"]
    # spAuth.spotify_object.token_secret = token_info["refresh_token"]
    # spAuth.spotify_object.expires_at = token_info["expires_at"]
    # spAuth.spotify_object.scope = token_info["scope"]
