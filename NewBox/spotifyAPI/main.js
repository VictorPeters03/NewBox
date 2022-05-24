import axios from "axios";
<script src="https://cdnjs.cloudfare.com/ajax/libs/axios/0.19.0/axios.min.js\"></script>

//POST REQUEST

function getArtist() {
    axios
        .get('https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-artist')
        .then(res => showOutput(res))
        .catch(err => console.error(err));
}

function getAlbumByArtist() {
    axios
        .get('https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-artists-albums')
        .then(res => showOutput(res))
        .catch(err => console.error(err));
}

function getAlbumByID() {
    axios
        .get('https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-album')
        .then(res => showOutput(res))
        .catch(err => console.error(err));
}

function getAlbumTracks() {
    axios
        .get('https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-albums-tracks')
        .then(res => showOutput(res))
        .catch(err => console.error(err));
}

function getTrackByID() {
    axios
        .get('https://developer.spotify.com/documentation/web-api/reference/#/operations/get-track')
        .then(res => showOutput(res))
        .catch(err => console.error(err));
}


//INTERCEPTING

axios.interceptors.request.use(config => {
    console.log(`${config.method.toUpperCase()}request sent to ${config.url} at ${new Date().getTime()}`);
    return config
}, error => {
    return Promise.reject(error)
});

//CUSTOM HEADERS

function customHeaders() {
    const config = {
        headers: {
            'Content-type': 'application/python',
            Authorization: 'spotifyHandler'
        }
    }
}