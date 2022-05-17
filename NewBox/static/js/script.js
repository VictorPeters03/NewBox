$(function() {
    $(".navbar-search").click(function(){
        $(this).hide();
        $(".top-navbar #logo, .navbar-search-settings").hide();
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
            $(".top-navbar #logo, .navbar-search-settings").show();
        }, 500);
    });
});