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
$('.pin').click(function(){
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    var blog_name = $(this).attr("name");
    var pin = '#pin'+blog_name;
    if ($(pin).attr("name") == "unpin"){
    console.log('pinning');
    var request = $.ajax({
        url: "/apis/pin/"+blog_name,
        method: "GET",
    }).done(function(){
        // $('.fa-map-pin').css("color", "red");
        $(pin).css("color", "red");
        // $(pin).val("pinned");
        $(pin).attr("name","pinned")
    })
    .fail(function() {
        $('#login-modal').modal();
    });
}
else if ($(pin).attr("name") == "pinned"){
    console.log('unpinning')
    var request = $.ajax({
        url: "/apis/pin/"+blog_name,
        type: 'DELETE',
    }).done(function(){
        // $('.fa-map-pin').css("color", "red");
        $(pin).css("color", "grey");
        // $(pin).val("unpin");
        $(pin).attr("name","unpin")
        document.location.reload(true)
    })
    .fail(function() {
        $('#login-modal').modal();
    });
}
});