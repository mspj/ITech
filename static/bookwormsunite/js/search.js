$(function () {
    $("#search").autocomplete({
        source: function (request, response) {
            $.getJSON("/autocomplete_search/?term=" + request.term, function (data) {
                response($.map(data.result, function (data) {
                    return {
                        label: data.label,
                        value: data.slug
                    };
                }));
            });
        },
        minLength: 2,
        select: function (event, ui) {
            goToReadathon(ui.item.label);
        }
    });

    function goToReadathon(slug_readathon) {
        location.href = "/readathon/" + slug_readathon;
    }
});