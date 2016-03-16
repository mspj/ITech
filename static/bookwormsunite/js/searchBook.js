$(function () {
    $("#searchBook").keyup(function (e) {
        if (e.keyCode == 13) {
            alert("Enter was pressed was presses");
            $.ajax({
                url: "https://www.goodreads.com/search/index.xml?key=MDJqEMH3YFyMuHGWqYCnHg&q="+this.value,
                method: 'get',
                dataType: 'xml',
                success: function (data) {
                    console.log($.parseXML(data));
                }
            });
        }
    });
});