$(function() {
    $(".navbar-search").click(function(){
        $(this).hide();
        $(".top-navbar h1, .navbar-search-settings").hide();
        $(".searchbar").focus().toggleClass('full-width').toggleClass('flex').val('');
        setTimeout(function (){
            $('#navbar-search').toggleClass('full-width').toggleClass('flex').val('');
            $('.navbar-search-small').show();
            $(".navbar-cross-small").show();
        }, 500);
    });

    $(".navbar-cross-small").click(function(){
        $(this).hide();
        $('.navbar-search-small').hide();
        $(".navbar-cross-small").hide();
        $('#navbar-search').focus().toggleClass('full-width').toggleClass('flex').val('');
        $(".searchbar").focus().toggleClass("full-width").toggleClass("flex").val('');
        setTimeout(function (){
            $(".navbar-search").show();
            $(".top-navbar h1, .navbar-search-settings").show();
        }, 500);
    });
});

function getSongs()
{
    document.getElementById("sub-container").innerHTML = "Hello songs"
}

function getDownloaded()
{
    document.getElementById("sub-container").innerHTML = "Hello downloaded"
}

const songs = document.querySelector(".button-songs")

const downloaded = document.querySelector(".button-downloaded")

songs.addEventListener("click", getSongs)
downloaded.addEventListener("click", getDownloaded)