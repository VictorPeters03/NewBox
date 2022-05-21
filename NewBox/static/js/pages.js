// import axios from "axios";

const CLIENT_ID = "ec41429613ba45c8984f3119527186ff"

const CLIENT_SECRET = "62547ecfa262441bb6789d1004b45e82"

const songs = document.querySelector(".button-songs")

const downloaded = document.querySelector(".button-downloaded")

const index = document.querySelector("#sub-container")

const logo = document.querySelector("#logo")

function getHomePage()
{
    index.innerHTML = ""
}

function getSongs()
{
    index.innerHTML = '<div id="songs-downloaded"></div>\n'

    let songs_downloaded = document.querySelector('#songs-downloaded')

    axios.get("https://api.spotify.com/v1/playlists/37i9dQZF1DX2LTcinqsO68/tracks?market=NL&limit=20",
        {
            headers:
            {
                "Content-Type": "application/json",
                "Authorization": "Bearer BQAhBFQeyIxdEqwRO7FIr1MnJFhN0aFTzeLGOZr9u2nJUwGgoxefGhW3vYtP775tXYgN3ispW2c0tUX8rftlnYPkWwOK5SLVKflPPz5IgCHCZ1MyuDMASP53u6xglDjZYZNPx4xY5KY-blIVHJSimv_CDcQND0v6NZg"
            }
        })
    .then(resp => {
        resp.data.items.forEach(element =>
            // console.log(element["track"]["artists"][0]["name"])
        songs_downloaded.innerHTML += '<div class="song-downloaded">\n' +
        '                       <div class="image"></div>' +
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


songs.addEventListener("click", getSongs)
downloaded.addEventListener("click", getDownloaded)
logo.addEventListener("click", getHomePage)