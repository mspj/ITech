$(document).foundation();

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$(function () {
    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

    $('#login_form').on('submit', function(event){
        event.preventDefault();

        $.ajax({
            type: 'POST',
            url: '/login/',
            data: $('#login_form').serialize(),
            dataType: 'json',
            encode: true,
            success: function(){
                //display success msg
            },
            fail: function(){
                //display failed msg
            }
        });
    });

    $('#register_form').on('submit', function(event){
        event.preventDefault();

        $.ajax({
            type: 'POST',
            url: '/register/',
            data: $('#register_form').serialize(),
            dataType: 'json',
            encode: true,
            success: function(){
                //display success msg
            },
            fail: function(){
                //display failed msg
            }
        });
    });
});