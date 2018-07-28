$(document).ready(function (){
    // if ($(window).width() < 690) {
    //     console.log('moblie');
    //     return $('.mainbar').addClass('navbar-expand-md');
    // }
   // $('.mainbar').removeClass('mobile');
});
FB.login(function(response) {
    if(response.authResponse) {
        FB.api('/me',function(response){
            console.log('hi' + response.name);
            console.log(response.email);
            var request = $.ajax({
                url: "/apis/login",
                method: "POST",
                contentType: "application/json",
                dataType: "json",
                data: JSON.stringify({
                    "username":response.email,
                    "password":response.name
                }),
            }).done(function(){
                document.location.reload(true);
            })
            .fail(function() {
                console.log(response);
                var register_fb = $.ajax({
                    url: "/apis/register",
                    method: "POST",
                    contentType: "application/json",
                    dataType: "json",
                    data: JSON.stringify({
                        "username":response.name,
                        "password":response.name,
                        "first_name":response.first_name,
                        "last_name":response.last_name,
                        "email":response.email
                    }),
                }).done(function(){
                    location.href = "/"
                    var request = $.ajax({
                        url: "/apis/login",
                        method: "POST",
                        contentType: "application/json",
                        dataType: "json",
                        data: JSON.stringify({
                            "username":response.email,
                            "password":response.name
                        }),
                    })
                })
                .fail(function() {
                    alert('fail');
                })
            });
        });

    }
})
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