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
    var lastScrollTop = 0;
    var nav = $('.mainbar');
    var nav_category = $('.nav-category');
    var nav_tag = $('.nav-tag');
    $(window).scroll(function(event){
       var st = $(this).scrollTop();
       //console.log(st);
       if (st > lastScrollTop && st > 56){
           // downscroll code
           nav.fadeOut(200);
           //nav.addClass('nav-up');
           if(st >= 305){
            nav_category.addClass('fixed');
            nav_tag.addClass('tag-fixed');
            nav_category.removeClass('nav-ontop-category');
            nav_tag.removeClass('nav-ontop-tag');
            //nav_category.addClass('nav-ontop-category');
            //nav_tag.addClass('nav-ontop-tag');
           }
           else{
            nav_category.removeClass('fixed');
            nav_tag.removeClass('tag-fixed');
            nav_category.removeClass('nav-ontop-category');
            nav_tag.removeClass('nav-ontop-tag');
           }
       } else{
          // upscroll code
          //console.log(st + $(window).height());
           if(st + $(window).height() < $(document).height()){
                //nav.removeClass('nav-up');
                nav.fadeIn(1);
                nav_category.addClass('fixed');
                nav_tag.addClass('tag-fixed');
                nav_category.addClass('nav-ontop-category');
                nav_tag.addClass('nav-ontop-tag');
                if(st <= 305){
                    nav_category.removeClass('fixed');
                    nav_tag.removeClass('tag-fixed');
                    nav_category.removeClass('nav-ontop-category');
                    nav_tag.removeClass('nav-ontop-tag');
                   }
        }
       }
       lastScrollTop = st;
    });
function reload_elements(){
    pathName = window.location.pathname;
    var element = $('.on-selected');
    element.removeClass('on-selected');
    if (location.pathname == "/") {
        $('#feed').addClass('on-selected');
    }
    // else {
    //     $('#trending-container').hide();
    // }
    if (pathName.search("category") != -1){
      let categoryName = pathName.substring(pathName.lastIndexOf('/') + 1);
      $( "#"+categoryName ).addClass( "on-selected" );
    }
    else if (pathName.search("tag") != -1){
        let tagName = pathName.substring(pathName.lastIndexOf('/') + 1);
        var element = $(".on-tagged");
        element.removeClass("on-tagged");
        $("#tag-"+tagName).addClass( "on-tagged");
        $("#"+tagName).prependTo(".tag-bar");
      }
}
$(document).ready(function() {
    // Highlight selected category  for category pages
    reload_elements();
    
    $('input.form-control').keypress(function (e) {
        if (e.which == 13) {
            console.log('hit enter');
          $('#search-form').submit();
          return false;
        }
      });
    $('div.category-title').click(function() {
        var category_path = $(this).attr('id');
        if(location.pathname == "/" && category_path == "feed") {
            $("html, body").animate({ scrollTop: 0 }, "slow");
            return false;
        }
        else if (location.pathname == "/category/"+category_path){
            $("html, body").animate({ scrollTop: 0 }, "slow");
            return false;
        }
        $('#blog-container').fadeOut();
        $('.loading').css("display", "block");
        var path = '/category/'+category_path;
        if(category_path == "feed"){
            path = "/";
        }
        $('#blog-container').load(path, function() {
            $('.loading').css("display", "none");
            $(this).fadeIn();
          });
        history.pushState(null, null, path);
        reload_elements();
    });
    $('div.tag-title').click(function() {
        var tag_path = $(this).attr('id');
        $('#blog-container').fadeOut();
        $('.loading').css("display", "block");
        var path = '/tag/'+tag_path;
        $('#blog-container').load(path, function() {
            $('.loading').css("display", "none");
            $(this).fadeIn();
          });
        history.pushState(null, null, '/tag/'+tag_path);
        reload_elements();
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