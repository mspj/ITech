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

    $('#login_form').on('submit', function (event) {
        event.preventDefault();
        $('#modalAlert').fadeIn();

        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: $('#login_form').serialize(),
            dataType: 'json',
            encode: true,
            success: function (data) {
                var alertArea = $('#modalAlert');
                var alertMsg = $('#modalAlertMsg');
                if (data.status === "success") {
                    alertMsg.text(data.msg);
                    alertArea.attr('class', 'callout success');
                    alertArea.fadeIn();
                    window.location = data.redirect_to;
                } else {
                    alertMsg.text(data.msg);
                    alertArea.fadeIn();
                }
            },
            error: function (data) {
                //display failed msg
            }
        });
    });

    $('#register_form').on('submit', function (event) {
        event.preventDefault();
        $('#modalAlert').fadeIn();

        $.ajax({
            type: 'POST',
            url: $(this).attr('action'),
            data: $('#register_form').serialize(),
            dataType: 'json',
            encode: true,
            success: function (data) {
                var alertArea = $('#modalAlert');
                var alertMsg = $('#modalAlertMsg');
                if (data.status === "success") {
                    alertMsg.text(data.msg);
                    alertArea.attr('class', 'callout success');
                    alertArea.fadeIn();
                    window.location = data.redirect_to;
                } else {
                    alertMsg.text(data.msg);
                    alertArea.fadeIn();
                }
            },
            error: function (data) {
                //display failed msg
            }
        });
    });
});