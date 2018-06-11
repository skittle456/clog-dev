
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
    $('button.close').click();
}

function register(){
    console.log('registering');
    $('button.close').click();
}
