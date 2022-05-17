const songs = document.querySelector(".button-songs")

const downloaded = document.querySelector(".button-downloaded")

const index = document.querySelector("#sub-container")

function getHomePage()
{
    index.innerHTML = ""
}

function getSongs()
{
    index.innerHTML = '<div id="songs-downloaded">\n' +
        '            <div class="song-downloaded">\n' +
        '                <h1>Song 1</h1>\n' +
        '            </div>\n' +
        '            <div class="song-downloaded">\n' +
        '                <h1>Song 2</h1>\n' +
        '            </div>\n' +
        '        </div>'
}

function getDownloaded()
{
    index.innerHTML = '<div id="songs-downloaded"></div>\n'

    let songs_downloaded = document.querySelector('#songs-downloaded')

    axios.get('https://datausa.io/api/data?drilldowns=Nation&measures=Population')
    .then(resp => {
        resp.data.data.forEach(element =>
            songs_downloaded.innerHTML += '<div class="song-downloaded">\n' +
        '                       <h1>' + element["Nation"] + '</h1>\n' +
        '                   </div>\n'
        )
    });
}

songs.addEventListener("click", getSongs)
downloaded.addEventListener("click", getDownloaded)