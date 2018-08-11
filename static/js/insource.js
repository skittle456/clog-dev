$.ajaxSetup({ 
    beforeSend: function(xhr, settings) {
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
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    } 
});

$(document).ready(function() {
    if ($(window).width() < 690) {
        console.log('moblie');
        return $('#vert-menu').hide();
    }
    $('.follow-btn').click(function(){
        var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
        if ($(this).attr("name") == "unfollow"){
        console.log('following');
        var request = $.ajax({
            url: "/apis/follow/"+$(this).attr("id"),
            method: "GET",
        }).done(function(){
            //$('.fa-map-pin').css("color", "red");
            $('.follow-btn').css("color", "white");
            $('.follow-btn').css("background-color", "#FFA300");
            $('.follow-btn').attr("name","followed")
            $('.follow-btn').text("Unfollow");
            //document.location.reload(true)
        })
        .fail(function() {
            $('#login-modal').modal();
        });
    }
    else if ($(this).attr("name") == "followed"){
        console.log('unfollowing')
        var request = $.ajax({
            url: "/apis/follow/"+$(this).attr("id"),
            type: 'DELETE',
        }).done(function(){
            // $('.fa-map-pin').css("color", "red");
            $('.follow-btn').css("color", "#FFA300");
            $('.follow-btn').css("background-color", "white");
            $('.follow-btn').attr("name","unfollow");
            $('.follow-btn').text("Follow");
            //document.location.reload(true)
        })
        .fail(function() {
            $('#login-modal').modal();
        });
    }
    });
    $('.pin-item').click(function(){
        if ($(this).attr("name") == "unpin"){
            console.log('pinning');
            var request = $.ajax({
                url: "/apis/pin/"+$(this).attr("id"),
                method: "GET",
            }).done(function(){
                //$('.fa-map-pin').css("color", "red");
                $('.pin-item').css("color", "white");
                $('.pin-item').css("background-color", "#f9a11d");
                $('.pin-item').css("border", "1px solid #f9a11d");
                $('.pin-item').attr("name","pinned")
                $('#pin-text').text("Unpin this post");
            })
            .fail(function() {
                $('#login-modal').modal();
            });
        }else if($(this).attr("name") == "pinned"){
            console.log('unpinning');
            var request = $.ajax({
                url: "/apis/pin/"+$(this).attr("id"),
                method: "DELETE",
            }).done(function(){
                //$('.fa-map-pin').css("color", "red");
                $('.pin-item').css("background-color", "grey");
                $('.pin-item').css("border", "1px solid white");
                $('.pin-item').attr("name","unpin")
                $('#pin-text').text("Pin this post");
            })
            .fail(function() {
                $('#login-modal').modal();
            });
        }
    });
    $('.like-btn').click(function(){
        if ($(this).attr("name") == "unlike"){
            console.log('liking');
            var request = $.ajax({
                url: "/apis/like/"+$(this).attr("id"),
                method: "GET",
            }).done(function(){
                //$('.fa-map-pin').css("color", "red");
                $('.like-btn').css("color", "#f9a11d");
                $('.like-btn').css("background-color", "white");
                $('.like-btn').attr("name","liked")
                var count = parseInt($('.like-num').text());
                console.log(count);
                count=count+1;
                $('.like-num').text(count);
            })
            .fail(function() {
                $('#login-modal').modal();
            });
        }else if($(this).attr("name") == "liked"){
            console.log('unliking');
            var request = $.ajax({
                url: "/apis/like/"+$(this).attr("id"),
                method: "DELETE",
            }).done(function(){
                //$('.fa-map-pin').css("color", "red");
                $('.like-btn').css("color", "white");
                $('.like-btn').css("background-color", "lightgrey");
                $('.like-btn').attr("name","unlike")
                var count = parseInt($('.like-num').text());
                console.log(count);
                count=count-1;
                $('.like-num').text(count);
            })
            .fail(function() {
                $('#login-modal').modal();
            });
        }
    });
$('div.back').click(function(){
    console.log('back clicked');
    window.history.back;
});
});