// import axios from "axios";

const CLIENT_ID = "ec41429613ba45c8984f3119527186ff"

const CLIENT_SECRET = "62547ecfa262441bb6789d1004b45e82"

const songs = document.querySelector(".button-songs")

const downloaded = document.querySelector(".button-downloaded")

const index = document.querySelector("#sub-container")

const logo = document.querySelector("#logo")

const settings = document.querySelector(".navbar-settings img")

function getHomePage()
{
    index.innerHTML = ""
}

function getSongs()
{
    index.innerHTML = '<div id="songs-downloaded"></div>\n'

    let songs_downloaded = document.querySelector('#songs-downloaded')

    axios.get("https://api.spotify.com/v1/playlists/37i9dQZF1DX2LTcinqsO68/tracks?market=NL&limit=10",
        {
            headers:
            {
                "Content-Type": "application/json",
                "Authorization": "Bearer BQBbtOZZJWxzpl0DH7o2UlZY5e_v86CD4n7M1zq4afcKcsBhidXDk34-UxPC5SCYtGdrZQxAm9mui55gscHIkpmm9cqQl4_xYxaG0HMEMR4U5TRJt_8-ZdKrhq3iMDaVhGddDfTbUxkTZxEeQMFu3J2ttQd_DQ4aA_zSMBSVf4FOGkPoOO2XLNna-tlSR0EMTFMbKFqQLpdenvRVVLFgMwhhw7JXR61Yfxxw"
            }
        })
    .then(resp => {
        resp.data.items.forEach(element =>
            // console.log(element["track"]["artists"][0]["name"])
        songs_downloaded.innerHTML += '<div class="song-downloaded">\n' +
        '                       <div class="album-cover"><img src="' + element["track"]["album"]["images"][2]["url"] + '" alt=""></div>' +
        '                       <div class="title-artist">' +
                '<div class="title"><p>' + element["track"]["name"] + '</p></div>' +
                '<div class="artist"><p>' + element["track"]['artists'][0]["name"] + '</p></div>' +
                '</div>' +
                '<div class="add-to-playlist"><img src="../static/images/Playlist.svg" alt="Add to playlist"></div>' +
        '                   </div>\n'
        )
    });
}

function getDownloaded()
{
    index.innerHTML = '<div id="songs-downloaded"></div>\n'

    let songs_downloaded = document.querySelector('#songs-downloaded')

    axios.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population')
    .then(resp => {
        resp.data.data.forEach(element =>
            songs_downloaded.innerHTML += '<div class="song-downloaded">\n' +
        '                       <div class="image"></div>' +
        '                       <div class="title-artist">' +
                '<div class="title"><p>' + element["Nation"] + '</p></div>' +
                '<div class="artist"><p>' + element["Year"] + '</p></div>' +
                '</div>' +
                '<div class="add-to-playlist"><img src="../static/images/Playlist.svg" alt="Add to playlist"></div>' +
        '                   </div>\n'
        )
    });
}

function getSettings()
{
    index.innerHTML = "<div id=\"settings\">\n" +
        "            <div class=\"setting\">\n" +
        "                <div class=\"setting-text\">\n" +
        "                    <h1>Dark mode</h1>\n" +
        "                </div>\n" +
        "                <div class=\"setting-switch\"></div>\n" +
        "            </div>\n" +
        "        </div>"


}


songs.addEventListener("click", getSongs)
downloaded.addEventListener("click", getDownloaded)
logo.addEventListener("click", getHomePage)
settings.addEventListener("click", getSettings)