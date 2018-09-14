$(document).ready(function (){
    $('.nav-brand').hide();
    $('body').click(function(evt){   
        if($(evt.target).is('.sidebar-collaspe')) {
            //event handling code
            $('#sidebar').toggleClass('active');
            $('.collapse.in').toggleClass('in');
            $('a[aria-expanded=true]').attr('aria-expanded', 'false');
            return
        }
        else if(!$(evt.target).is('.fa-search') && $(window).width() < 690) {
            $('.searchbar').hide();
            $('.nav-sm').fadeIn();
        }

        $('#sidebar').addClass('active')
        $('.collapse.in').addClass('in');
        $('a[aria-expanded=false]').attr('aria-expanded', 'True');
    });
    if ($(window).width() < 690) {
        //return $('.mainbar').addClass('navbar-expand-md');
        console.log('moblie');
        // $('.search-item').hide();
        $('.logo-brand').remove();
        $('.nav-md').remove()
        $('.searchbar').hide();
    }
    else{
        $('.nav-sm').remove();
        $('.nav-search').remove();
        // $('.mobile-search').hide();
        // $('.search-button').hide()
        // $('#sidebar').toggleClass('active');
    }
    $('.search-btn').on('click', function(){
        $('.nav-sm').hide();
        $('.searchbar').fadeIn();
    })
   // $('.mainbar').removeClass('mobile');
    // $('#sidebarCollapse').on('click', function () {
    //     $('#sidebar').toggleClass('active');
    // });
    // $('.search-button').on('click',function(){
    //     $('.mobile-search').show();
    //     $('.search-item').show();
    // })
    // $('.search-item').on('focus', function(){
    //     $('navbar-brand').hide()
    // })
    // $('.search-item').on('focusout', function(){
    //     $('navbar-brand').show()
    // })
});

// FB.login(function(response) {
//     if(response.authResponse) {
//         FB.api('/me',function(response){
//             console.log('hi' + response.name);
//             console.log(response.email);
//             var request = $.ajax({
//                 url: "/apis/login",
//                 method: "POST",
//                 contentType: "application/json",
//                 dataType: "json",
//                 data: JSON.stringify({
//                     "username":response.email,
//                     "password":response.name
//                 }),
//             }).done(function(){
//                 document.location.reload(true);
//             })
//             .fail(function() {
//                 console.log(response);
//                 var register_fb = $.ajax({
//                     url: "/apis/register",
//                     method: "POST",
//                     contentType: "application/json",
//                     dataType: "json",
//                     data: JSON.stringify({
//                         "username":response.name,
//                         "password":response.name,
//                         "first_name":response.first_name,
//                         "last_name":response.last_name,
//                         "email":response.email
//                     }),
//                 }).done(function(){
//                     location.href = "/"
//                     var request = $.ajax({
//                         url: "/apis/login",
//                         method: "POST",
//                         contentType: "application/json",
//                         dataType: "json",
//                         data: JSON.stringify({
//                             "username":response.email,
//                             "password":response.name
//                         }),
//                     })
//                 })
//                 .fail(function() {
//                     alert('fail');
//                 })
//             });
//         });

//     }
// })
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

function edit_profile(user_id){
    if($('#register-password').val() != $('#confirm-password').val()){
        return alert('incorrect password');
    }
    var request = $.ajax({
        url: "/apis/edit_profile"+user_id,
        method: "PATCH",
        contentType: "application/json",
        dataType: "json",
        data: JSON.stringify({
            "username":$('#account-username').val(),
            "password":$('#account-password').val(),
            "first_name":$('#first_name').val(),
            "last_name":$('#last_name').val(),
            "email":$('#setting-email').val(),

        }),
    }).done(function(){
        alert("success");
    })
    .fail(function() {
        alert("fail")
    });
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