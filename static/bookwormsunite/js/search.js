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
            event.preventDefault();
            this.value = ui.item.label;
            goToReadathon(ui.item.value);
        }
    });

    function goToReadathon(slug) {
        location.href = "/readathon/" + slug;
    }
});