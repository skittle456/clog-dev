// jQuery(function($) {
//     $("img.lazy").lazyload({
//     threshold: 50,
//     data_attribute: "orig"
// });
// $(window).trigger("scroll");
// });
var blogs = null;
$('div#demo').on('slide.bs.carousel', function (e) {
        console.log('sliding');
        var $e = $(e.relatedTarget);
        var idx = $e.index();
        var itemsPerSlide = 4;
        var totalItems = $('.carousel-item').length;
        
        if (idx >= totalItems-(itemsPerSlide-1)) {
            var it = itemsPerSlide - (totalItems - idx);
            for (var i=0; i<it; i++) {
                // append slides to end
                if (e.direction=="left") {
                    $('.carousel-item').eq(i).appendTo('.carousel-inner');
                }
                else {
                    $('.carousel-item').eq(0).appendTo('.carousel-inner');
                }
            }
        }
    });
$(document).ready(function() {
    // Highlight selected category  for category pages
    pathName = window.location.pathname;
    if (location.pathname == "/") {
        $('#category-feed').addClass('on-selected');
    } else {
        $('#trending-container').hide();
    }
    if (pathName.search("category") != -1){
      let categoryName = pathName.substring(pathName.lastIndexOf('/') + 1);
      $( "#category-"+categoryName ).addClass( "on-selected" );
      if ($('#category-feed').hasClass('on-selected')){
        $('#category-feed').removeClass('on-selected');
    }
    }
    else if (pathName.search("tag") != -1){
        let tagName = pathName.substring(pathName.lastIndexOf('/') + 1);
        $( "#tag-"+tagName ).addClass( "on-tagged" );
      }
    $('input.form-control').keypress(function (e) {
        if (e.which == 13) {
            console.log('hit enter');
          $('#search-form').submit();
          return false;
        }
      });
    // $("#search-form").on("change keyup paste", function(){
    //     console.log($(this).val())
    //     let blogs_list = blogs();
    //     console.log(blogs_list[0].blog.title);
    // })
});
// function passBlogs(blogs_list){
//     window.blogs = blogsList;
//     console.log('pass');
// }
// import objects from './templates/index.html';

// function mySearch() {
//     console.log(objects.blogs[0].fields.title);
//     //console.log('this is blogs[0]'+blogs[0].fields.title);
// }