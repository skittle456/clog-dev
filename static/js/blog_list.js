$('.pin').click(function(){
    console.log('pinning');
    console.log($(this).attr("name"));
    var request = $.ajax({
        url: "/apis/pin/"+$(this).attr("name"),
        method: "GET",
    }).done(function(){
        console.log('blog has been pinned')
    })
    .fail(function() {
        $('#login-modal').modal();
    });
});