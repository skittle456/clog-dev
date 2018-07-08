$(document).ready(function (){
    // if ($(window).width() < 690) {
    //     console.log('moblie');
    //     return $('.mainbar').addClass('navbar-expand-md');
    // }
   // $('.mainbar').removeClass('mobile');
});
function post_feedback(){
    console.log($('textarea#message-text.form-control').val());
    console.log($('input#email.form-control').val());
    var request = $.ajax({
        url: "/apis/feedback_list",
        method: "POST",
        contentType: "application/json",
        dataType: "json",
        data: JSON.stringify({
            "email":$('input#email.form-control').val(),
            "feedback_message":$('textarea#message-text.form-control').val()
        }),
    }).done(function(){
        $('input#email.form-control').val('');
        $('textarea#message-text.form-control').val('');
        $('button.close').click();
        alert("Thank you for feedback");
    })
    .fail(function() {
        alert("fail")
    });
}


function login(){
    console.log('logging in');
    var request = $.ajax({
        url: "/apis/login",
        method: "POST",
        contentType: "application/json",
        dataType: "json",
        data: JSON.stringify({
            "username":$('#login-username').val(),
            "password":$('#login-password').val()
        }),
    }).done(function(){
        document.location.reload(true);
    })
    .fail(function() {
        alert("authentication fail")
    });
    $('button.close').click();
}

function register(){
    console.log('registering');
    var request = $.ajax({
        url: "/apis/register",
        method: "POST",
        contentType: "application/json",
        dataType: "json",
        data: JSON.stringify({
            "username":$('#register-username').val(),
            "password":$('#register-password').val(),
            "first_name":$('#first_name').val(),
            "last_name":$('#last_name').val(),
            "email":$('#register-email').val(),
        }),
    }).done(function(){
        location.href = "/"
    })
    .fail(function() {
        alert("unable to register")
    });
    $('button.close').click();
}

function logout(){
    console.log('logging out');
    console.log('')
    var request = $.ajax({
        url: "/apis/logout",
        method: "GET",

    }).done(function(){
        location.href = "/"
    })
    .fail(function() {
        alert("authentication fail")
    });
    $('button.close').click();
}