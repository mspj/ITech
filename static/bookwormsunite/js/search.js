$(function () {
    $("#search").autocomplete({
        source: function (request, response) {
            $.getJSON("/autocomplete_search/?term=" + request.term, function (data) {
                response($.map(data.result, function (data) {
                    return {
                        label: data.slug,
                        value: data.label
                    };
                }));
            });
        },
        minLength: 2,
        select: function (event, ui) {
            goToReadathon(ui.item.slug);
        }
    });

    function goToReadathon(slug_readathon) {
        location.href = "/readathon/" + slug_readathon;
    }
});