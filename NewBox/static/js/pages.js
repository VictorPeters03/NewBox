const CLIENT_ID = "ec41429613ba45c8984f3119527186ff"

const CLIENT_SECRET = "62547ecfa262441bb6789d1004b45e82"

const songs = document.querySelector(".button-songs")

const downloaded = document.querySelector(".button-downloaded")

const index = document.querySelector("#sub-container")

const logo = document.querySelector("#logo")

const settings = document.querySelector(".navbar-settings img")

const search = document.querySelector(".navbar-search-small img")

const query = document.querySelector("#navbar-search");

const queue = document.querySelector(".button-one")


function getSettings()
{
    index.innerHTML = "<div id=\"settings\">\n" +
        "                    <h1>Rasberry Pi Settings</h1>\n" +
        "                    <p onclick='pi_reboot()'>Reboot</p>\n" +
        "                    <p onclick='pi_shutdown()'>Shutdown</p>\n" +
        "                    <H1>Queue</H1>\n" +
        "                    <p>Show list</p>\n" +
        "                </div>\n" +
        "                <div class=\"setting-switch\"></div>\n" +
        "            </div>\n" +
        "        </div>"
}

function pi_reboot()
{
    axios.put("http://127.0.0.1:8086/use/reboot")
    .then(resp => {
        console.log(resp)
    })
}

function pi_shutdown()
{
    axios.put("http://127.0.0.1:8086/use/reboot")
    .then(resp => {
        console.log(resp)
    })
}

function queueSong(uri)
{
    axios.put("http://127.0.0.1:8086/use/queue/spotify:track:5oD2Z1OOx1Tmcu2mc9sLY2")
    .then(resp => {
        console.log(resp)
    })
}

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
                "Authorization": "Bearer BQA_u9S3wDU9ImKOTR3ZjXQujmXdjebQH0s-ugtjKXWLjJ72-CFdWRk5dNvZzS8yDL73dU1h7kcMlcvg-CRyq4p3JQT8sYrquKl3kOhVjFgDs7ViDF4OztjYLKomlW8pck_cw8QA1LEWZQYbZQyHVEUGN9U3T5wcwtRKXWYKcBHC_sEKb_0XVXpgauzWzY4N9tIau8nRr9LAI839KPj6YTAH17DHsA1gHmU7"
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

    axios.get('http://127.0.0.1:8086/use/getsongs')
    .then(resp => {
        // console.log(resp)
        resp.data.forEach(element =>
            // console.log(element)
            songs_downloaded.innerHTML += '<div class="song-downloaded">\n' +
        '                       <div class="image"></div>' +
        '                       <div class="title-artist">' +
                '<div class="title"><p>' + element["title"] + '</p></div>' +
                '<div class="artist"><p>' + element["artist"] + '</p></div>' +
                '</div>' +
                '<div class="add-to-playlist"><img src="../static/images/Playlist.svg" alt="Add to playlist" onclick="queueSong(' + "'" + element["uri"] + "'" + ')"></div>' +
        '                   </div>\n'
        )
    })
}

function searchSong()
{
    index.innerHTML = '<div id="songs-downloaded"></div>\n'
    query.focus()

    let songs_downloaded = document.querySelector('#songs-downloaded')

    axios.get('http://127.0.0.1:8086/use/search/' + query.value)
    .then(resp => {
        resp.data.forEach(element =>
            // console.log(element)
            songs_downloaded.innerHTML += '<div class="song-downloaded">\n' +
        '                       <div class="image"></div>' +
        '                       <div class="title-artist">' +
                '<div class="title"><p>' + element["title"] + '</p></div>' +
                '<div class="artist"><p>' + element["artist"] + '</p></div>' +
                '</div>' +
                '<div class="add-to-playlist"><img src="../static/images/Playlist.svg" alt="Add to playlist"></div>' +
        '                   </div>\n'
        )
    })
}

function queueSong(uri)
{
    axios.put("http://127.0.0.1:8086/use/queue/spotify:track:5oD2Z1OOx1Tmcu2mc9sLY2")
    .then(resp => {
        console.log(resp)
    })
}

function getQueue()
{
    axios.get("http://127.0.0.1:8086/use/getqueue")
    .then(resp => {
        console.log(resp)
    })
}

songs.addEventListener("click", getSongs)
downloaded.addEventListener("click", getDownloaded)
logo.addEventListener("click", getHomePage)
settings.addEventListener("click", getSettings)
search.addEventListener("click", searchSong)
queue.addEventListener("click", getQueue)
