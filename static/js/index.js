jQuery(function($) {
    $("img.lazy").lazyload({
    threshold: 50,
    data_attribute: "orig"
});
window.onload = function(){
    this.trigger("scroll");
}
$(window).trigger("scroll");
});