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

    axios.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population')
    .then(resp => {
        resp.data.data.forEach(element =>
            songs_downloaded.innerHTML += '<div class="song-downloaded">\n' +
        '                       <h1>' + element["Year"] + '</h1>\n' +
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