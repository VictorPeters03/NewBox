import spotipy
from .secrets import SPOTIFY_REDIRECT_URI, USER, SCOPES, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET
from spotipy.oauth2 import SpotifyOAuth

spAuth = spotipy.oauth2.SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET,
                                     redirect_uri=SPOTIFY_REDIRECT_URI, scope=SCOPES)

authCode = spAuth.parse_response_code(
    url='http://localhost:8080/?code=AQBGLkkQeFBHJJGvgX1wu0rS0xXvxVa6kvFHlOJ6Ot00nIqg427js3Vmo0H6UWVJBlDuU0AZV4n0Q5w_ABAzRidI1xmtHWoR5xkXCfKGS70TTUm_7vim3njCknbN-yPA6ar4Fp8CxSjit4ALIkHeMCPDd0mfIIfIfV-pbxdZSTZWfr2FMXsaqKLc3F-3TsjrzX-ipQPFs28F5GDB_mXpGLDhuRa-OoymETTy-AtNzVY2kGz5fRiC0rnfdkEMuVUOnJDD9Rq4yWdwmZ_UwEcBVdiPipK2kJPcX9lMmbuo3uivBCCxToAQzUnJ99VGGPrVAHR4ECMXlrxF0V3zCdDBgFS-wOB68RtGw9dJUg10JjjlHRJfL4XtYxX7RHYt_qrgbHPQ2YNFEZRJ-Tdh_246v8j1fEjjlT7vc1Ehg4K7P8GOiiHBEzv9LBEn8-dwIIr1n1ITApED9DJ2nRUfQPNYofjXFiQnzyHBPD0XEDe9XX8SS4tUFxMZIVW25X0D04tf_2lJmkuqRTtrYgIMjjXLv9vA48lEu9ZvdaR2V_vNtgmhsG4bZFcY2GG4RE7Yydyv9JSRp3aWoo7Pk3tbqTZLa1vF3Efa1Kbx77ifjSDAtwU57JMbS5btqhMshRGWgvbz_s4gjMpuz5sryhllIU7E-dKfr8f8T_kmhG_QeAmHOgQVEmXqqqVeNGo'
)


if spAuth.get_cached_token()['access_token'] is None:
    token = spAuth.get_access_token(code=authCode, as_dict=True)

token = spAuth.get_cached_token()['access_token']
refreshToken = spAuth.get_cached_token()['refresh_token']
# spAuth.refresh_access_token(refreshToken)

spotifyHandler = spotipy.Spotify(token)

