jQuery(function($) {
    $("img.lazy").lazyload({
    threshold: 50,
    data_attribute: "orig"
});
$(window).trigger("scroll");
});
