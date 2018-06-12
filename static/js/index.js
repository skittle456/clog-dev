jQuery(function($) {
    $("img.lazy").lazyload({
    threshold: 50,
    data_attribute: "orig"
});
$(window).trigger("scroll");
});
$(document).ready(function() {
    // Highlight selected category  for category pages
    pathName = window.location.pathname;
    if (pathName.search("category") != -1){
      let categoryName = pathName.substring(pathName.lastIndexOf('/') + 1);
      $( "#category-"+categoryName ).addClass( "active" );
    }
    
})
