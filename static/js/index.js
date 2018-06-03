jQuery(function($) {
    $("img.lazy").lazyload({
    threshold: 50
});
$(window).on('load', function(){
    $("html,body").trigger("scroll");
})
});