$('.pin').click(function(){
    console.log('pinning');
    console.log($(this).val());
    var request = $.ajax({
        url: "/apis/pin/"+$(this).val(),
        method: "GET",
    }).done(function(){
        console.log('blog has been pinned')
    })
    .fail(function() {
        alert("unable to pin")
    });
});