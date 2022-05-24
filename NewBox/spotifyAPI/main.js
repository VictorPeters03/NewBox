import axios from "axios";

//POST REQUEST

function getArtist() {
    axios.post('https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-artist'), {
        name: ['name'],
        uri: ['uri']
    }
        .then(res => showOutput(res))
        .catch(err => console.error(err));
}

<script src="https://cdnjs.cloudfare.com/ajax/libs/axios/0.19.0/axios.min.js\"></script>

//INTERCEPTING

axios.interceptors.request.use(config => {
    console.log(`${config.method.toUpperCase()}request sent to ${config.url} at ${new Date().getTime()}`);
    return config
}, error => {
    return Promise.reject(error)
});