const songs = document.querySelector(".button-songs")

const downloaded = document.querySelector(".button-downloaded")

const index = document.querySelector("#sub-container")

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
    index.innerHTML = '<div id="songs-downloaded">\n' +
            '            <div class="song-downloaded">\n' +
            '                <h1>Song 1</h1>\n' +
            '            </div>\n' +
            '            <div class="song-downloaded">\n' +
            '                <h1>Song 2</h1>\n' +
            '            </div>\n' +
            '        </div>'
}

songs.addEventListener("click", getSongs)
downloaded.addEventListener("click", getDownloaded)