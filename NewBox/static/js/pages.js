const songs = document.querySelector(".button-songs")

const downloaded = document.querySelector(".button-downloaded")

const index = document.querySelector("#sub-container")

const logo = document.querySelector("#logo")

const settings = document.querySelector(".navbar-settings img") //settings

const search = document.querySelector(".navbar-search-small img")

const query = document.querySelector("#navbar-search");

const queue = document.querySelector(".button-one")

const maxVolume = document.querySelector("#maxVolume")

const minVolume = document.querySelector("#minVolume")

const queueList = document.querySelector("#queue")

function getSettings()
{
    index.innerHTML = "<div id=\"settings\">\n" +
    "                    <h1>Rasberry Pi Settings</h1>\n" +
    "                    <button onclick='pi_reboot()'>Reboot</button>\n" +
    "                    <button onclick='pi_shutdown()'>Shutdown</button>\n" +
    "                    <h1>Volume Settings</h1>\n" +
    "                   <form name='setVolume' target='#here' method='post'>" +
    "                       <label for='maxVolume'></label>" +
    "                           <input type='text' name='maxVolume' id='maxVolume' placeholder='Type here to set max volume'>\n" +
    "                       </br>" +
    "                   </form>" +
    "                   <form name='setVolume' target='#here' method='post'>" +
    "                       <label for='minVolume'></label>" +
    "                           <input type='text' name='minVolume' id='minVolume' placeholder='Type here to set min volume'>\n" +
    "                       </form>" +
    "                    <h1>LED Settings</h1>\n" +
    "                   <label class='switch'>\n" +
    "                       <input type='checkbox'>" +
    "                       <span class='slider round'></span>" +
    "                   </label>" +
    "                    <h1>Queue</h1>\n" +
    "                    <button onclick='get_queue()'>Load the queue</button>\n"
}

function delete_from_queue(uri)
{
    axios.put("http://10.110.110.119:8000/admin/remove/" + uri)
        .then(resp => {
            console.log(resp)
        })
}

function set_max_vol()
{
    axios.put("http://10.110.110.119:8000/adminpanel/maxvolume/" + maxVolume.value)
        .then(resp => {
            console.log(resp)
        })
}

function set_min_vol(){
    axios.put("http://10.110.110.119:8000/adminpanel/minvolume/" + minVolume.value)
        .then(resp => {
            console.log(resp)
        })
}

function get_queue()
{
    queueList.innerHTML = ""
    axios.get("http://10.110.110.119:8000/use/getQueue")
    .then(resp => {
        console.log(resp)
        resp.data.forEach(element =>
            queueList.innerHTML +=
            '<div class="title" style="padding: 0 20px"><p>' + element["track"] + '</p></div>' +
            '<div class="artist" style="padding: 0 20px"><p>' + element["artist"] + '</p></div>' +
            '<div class="remove-songs" style="padding: 0 20px"><button onclick="delete_from_queue(' + "'" + element["uri"] + "'" + ')">Remove</button></div>'
        )
    })
}

function pi_reboot(){
    axios.get("http://10.110.110.119:8000/use/reboot")
    .then(resp => {
        console.log(resp)
    })
}

function pi_shutdown(){
    axios.get("http://10.110.110.119:8000/use/shutdown")
    .then(resp => {
        console.log(resp)
    })
}

function get_queue_title() {
    axios.put("/use/getqueuetitle")
    .then(resp => {
        console.log(resp)
    })
}



function queueSong(uri){
    axios.put("/use/queue/spotify:track:5oD2Z1OOx1Tmcu2mc9sLY2")
    .then(resp => {
        console.log(resp)
    })
}

function getHomePage(){
    index.innerHTML = ""
}

function getSongs(){
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

function getDownloaded(){
    index.innerHTML = '<div id="songs-downloaded"></div>\n'

    let songs_downloaded = document.querySelector('#songs-downloaded')

    axios.get('/use/getsongs')
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

function searchSong(){
    index.innerHTML = '<div id="songs-downloaded"></div>\n'
    query.focus()

    let songs_downloaded = document.querySelector('#songs-downloaded')

    axios.get('/use/search/' + query.value)
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

function getQueue(){
    axios.get("/use/getqueue")
    .then(resp => {
        console.log(resp)
    })
}

function skip()
{
    axios.put("http://127.0.0.1:8000/use/skip")
}

songs.addEventListener("click", getSongs)
downloaded.addEventListener("click", getDownloaded)
logo.addEventListener("click", getHomePage)
settings.addEventListener("click", getSettings)
search.addEventListener("click", searchSong)
queue.addEventListener("click", getQueue)
