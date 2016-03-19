$(function () {
    $("#twitter").ready(function () {
        $.ajax({
            url: encodeURI("/twitter/" + $("#hashtag").text()),
            method: 'GET',
            success: function (data) {
                if (data.status == 'success') {

                    var tweets_res = "<ul>";
                    var tweets = data.data;
                    if(tweets.length==0){
                        tweets_res += "No tweets in past 7 days"
                    }
                    for (var i = 0; i < tweets.length; i++) {
                        //tweets[i].created_at.substr(0,10)
                        if (tweets[i].media != null) {
                            tweets_res += '<li><img id="profile_image" src="' + tweets[i].profile_image_url + '"/> <span id="username">' + tweets[i].profile_username + '</span> <span id="created_at">' + tweets[i].created_at.substr(0,10) + '</span> <span id="text">' + tweets[i].text + '</span><img id="media" src="' + tweets[i].media + '"/> ' + ' </li> ';
                        } else {
                            tweets_res += '<li><img id="profile_image" src="' + tweets[i].profile_image_url + '"/> <span id="username">' + tweets[i].profile_username + '</span> <span id="created_at">' + tweets[i].created_at.substr(0,10) + '</span> <span id="text">' + tweets[i].text + ' </li> ';

                        }
                    }

                    tweets_res += "</ul>";

                    $('#twitter').html(tweets_res);

                } else {
                    console.log(data.msg)
                }
            },
            error: function (data) {
                //display failed msg
            }
        });

    });
});