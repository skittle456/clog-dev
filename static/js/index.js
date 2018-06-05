jQuery(function($) {
    $("img.lazy").lazyload({
    threshold: 50,
    data_attribute: "orig"
});
$(window).on('load', function(){
    $("html,body").trigger("scroll");
})
});