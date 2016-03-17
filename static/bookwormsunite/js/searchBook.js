$(function () {
    $("#searchBook").keyup(function (e) {
        if (e.keyCode == 13) {
            $.ajax({
                url: "/search/books/" + encodeURIComponent(this.value),
                method: 'GET',
                success: function (data) {

                    console.log(data);

                    if (data.status == 'success') {

                        var searchRes = "<ul style='list-style-type:none' class='search-result-box'>";
                        var books = data.data;

                        for (var i = 0; i < books.length; i++) {
                            searchRes += '<li><span style="display: none;">' + books[i].id + '</span><img src="' + books[i].cover_url + '"/>' + books[i].title + ',' + books[i].author + ',' + ' </li> ';
                        }

                        searchRes += "</ul>";

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

    $("#searchResult").on('click', 'li', function () {
        var booksSel='';
        if($('#bookList').html()!=null) {
            booksSel = $('#bookList').html();
        }
        booksSel += "<li>"+$(this).html()+"</li>";
        $('#bookList').html(booksSel);
    });

    $('#saveBook').on('click', 'bookList', function (event) {
        event.preventDefault();
        $('#modalAlert').fadeIn();
        console.log("hello: "+$('#bookList').text());
        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: $('#register_form').serialize(),
            dataType: 'json',
            success: function (data) {
                if (data.status === "success") {

                } else {

                }
            },
            error: function (data) {
                //display failed msg
            }
        });
    });
});