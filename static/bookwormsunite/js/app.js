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

function join_readathon(readathon_slug) {

    $.ajax({
            type: 'POST',
            url: "/readathon/" + readathon_slug + "/join/",
            success: function (data) {

                if (data.status == 'success') {
                    $('#readathon-join-section').html('<a href="#" class="button readathon-join-btn joined" id="readathon-quit-btn">Joined</a>');
                } else {
                    alert('could not join the readathon');
                }
            },
            error: function (data) {
                alert('could not join the readathon');
            }
        }
    )
}

function updateCalendar(offset) {

    // Check to see if the counter has been initialized
    if (typeof updateCalendar.counter == 'undefined') {
        // It has not... perform the initialization
        updateCalendar.counter = offset;
    } else {
        updateCalendar.counter = updateCalendar.counter + offset;
    }

    $.ajax({
        type: 'GET',
        url: "/calendar/" + updateCalendar.counter,
        success: function (data) {

            $('#readathon-calendar-month').html(data.month);

            var cal = "";

            for (var i = 0; i < data.calendar_obj.length; i++) {
                cal = cal + "<div class='large-1 day' style='cursor: pointer;'>" +
                    "<div style='margin-bottom: 0.5rem;'>" + data.calendar_obj[i].day + "</div>";

                for (var j = 0; j < data.calendar_obj[i].readathons.length; j++) {
                    cal = cal + "<div class='calendar-event'><a href=\"/readathon/" +
                        data.calendar_obj[i].readathons[j].slug +
                        "\">" + data.calendar_obj[i].readathons[j].name + "</a></div>";
                }

                cal = cal + "</div>";
            }

            $('#readathon-calendar-events').html(cal);
        },
        error: function (data) {
            //display failed msg
        }
    })

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

    $('#readathon-calendar-left').click(function () {
        updateCalendar(-1);
    });

    $('#readathon-calendar-right').click(function () {
        updateCalendar(1);
    });

    //$('#readathon-join-btn').preventDefault()
    $('#readathon-join-btn').click(function (e) {
        e.preventDefault();
        join_readathon(this.name);
    });

    //$('#profile-uploadimg-icon').click(function () {
    //    $("#upload_pic_form").click();
    //});

});
