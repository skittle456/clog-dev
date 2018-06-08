jQuery(function($) {
    $("img.lazy").lazyload({
    threshold: 50,
    data_attribute: "orig"
});
$(window).trigger("scroll");
});
$(document).ready(function() {
    $(".text-muted").click(function (){
        $(this).addClass("active");
        $(".text-muted").find(".active").removeClass("active");
    })
})
