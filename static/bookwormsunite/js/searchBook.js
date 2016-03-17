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
                            searchRes += '<li><span id="bookID" style="display: none;">' + books[i].id + '</span><img id="bookCover" src="' + books[i].cover_url + '"/><span id="bookTitle">' + books[i].title + '</span>,<span id="bookAuthor">' + books[i].author + '</span>,' + ' </li> ';
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
        var booksSel = '';
        if ($('#bookList').html() != null) {
            booksSel = $('#bookList').html();
        }
        booksSel += "<li>" + $(this).html() + "</li>";
        $('#bookList').html(booksSel);
    });

    $('#saveBook').click(function (e) {
        e.preventDefault();
        $('#modalAlert').fadeIn();
        //$('#challengeModal').fadeOut();
        //$('#challenge-join-btn').fadeIn();
        var challengeID = $('#cur_challenge_id').text();
        var books = [];
        var jsonData = {};
        $('#bookList').find('li').each(function () {
            jsonData['challenge_id'] = challengeID;
            jsonData['id'] = $(this).children("#bookID").text();
            jsonData['cover'] = $(this).children("#bookCover").attr('src');
            jsonData['title'] = $(this).children("#bookTitle").text();
            jsonData['author'] = $(this).children("#bookAuthor").text();
            books.push(jsonData);
        });

        $.ajax({
            type: 'POST',
            url: "/save_accomplishment/",
            data: {"books": JSON.stringify(books)},
            dataType: 'json',
            success: function (data) {
                var alertArea = $('#modalAlert');
                var alertMsg = $('#modalAlertMsg');
                if (data.status === "success") {
                    alertMsg.text("Add Books Success");
                    alertArea.attr('class', 'callout success');
                    alertArea.fadeIn();
                    window.location.reload();
                } else {
                    alertMsg.text("Please Try Again!");
                    alertArea.fadeIn();
                }
            },
            error: function (data) {
                //display failed msg
            }
        });

    });


});