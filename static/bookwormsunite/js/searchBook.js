$(function () {
    $("#searchBook").keyup(function (e) {
        if (e.keyCode == 13) {

            $.ajax({
                url: "/search/books/" + encodeURIComponent(this.value),
                method: 'GET',
                success: function (data) {

                    console.log(data);

                    if (data.status == 'success') {

                        var searchRes = "";
                        var books = data.data;

                        for (var i = 0; i < books.length; i++) {
                            searchRes += '<p> ' + books[i].title + ',' + books[i].author + ',' + ' </p>';
                        }

                        $('#searchResult').html(searchRes);

                    } else {
                        console.log(data.msg)
                    }
                },
                error: function (data) {
                    //display failed msg
                }
            });
        }
    });

    //$("#searchResult").click(function (e) {
    //    $('#booksSelected').html("<p>"+$('#searchResult').find('p:eq(0s)').text()+"</p>")
    //    console.log($('#searchResult').find('p:eq(0)').text());
    //
    //});
});