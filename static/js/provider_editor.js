function edit_provider_profile(){
    var request = $.ajax({
        url: "/apis/edit_provider_profile",
        method: "PATCH",
        contentType: "application/json",
        dataType: "json",
        data: JSON.stringify({
            "provider_name":$('input#provider_name.form-control').val(),
            "favicon_url":$('input#img-url.form-control').val()
        }),
    }).done(function(){
        alert("success");
    })
    .fail(function() {
        alert("fail")
    });
}