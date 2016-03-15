$(function () {
    $("#search").autocomplete({
        source: "/autocomplete_search/",
        minLength: 2,
        select: function(event, ui) {
            goToReadathon(ui.item.slug);
        }
    });

    function goToReadathon(slug_readathon) {
        location.href="/readathon/" + slug_readathon;
    }
});