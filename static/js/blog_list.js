$('.pin').click(function(){
    console.log('pinning');
    console.log($(this).attr("name"));
    var request = $.ajax({
        url: "/apis/pin/"+$(this).attr("name"),
        method: "GET",
    }).done(function(){
        $('.fa-map-pin').css("color", "red");
        console.log('blog has been pinned')
    })
    .fail(function() {
        $('#login-modal').modal();
    });
});