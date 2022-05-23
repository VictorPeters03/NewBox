import axios from "axios";

//POST REQUEST

function getArtist() {
    axios({
        method: 'post',
        url: 'https://developer.spotify.com/documentation/web-api/reference/#/operations/get-an-artist'
    })
        .then(res => showOutput(res))
        .catch(err => console.error(err));
}

<script src="https://cdnjs.cloudfare.com/ajax/libs/axios/0.19.0/axios.min.js\"></script>

