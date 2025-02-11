$.ajaxSetup({ 
    beforeSend: function(xhr, settings) {
        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                    var cookie = jQuery.trim(cookies[i]);
                    // Does this cookie string begin with the name we want?
                    if (cookie.substring(0, name.length + 1) == (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    } 
});
function generateNewFileName(s){
    var now = new Date();
    var possible = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    var extension = s.substring(s.lastIndexOf('.')); 
    var newName = now.getTime();
    for (var i = 0; i < 8; i++) newName += possible.charAt(Math.floor(Math.random() * possible.length))
    return newName+extension;
}
var quill = new Quill('#editor-container', {
    modules: {
        toolbar: [
        ['bold', 'italic'],
        ['link', 'blockquote', 'code-block', 'image', 'video'],
        [{ list: 'ordered' }, { list: 'bullet' }],
        [{ 'script': 'sub'}, { 'script': 'super' }],      // superscript/subscript
        [{ 'indent': '-1'}, { 'indent': '+1' }],          // outdent/indent
        [{ 'direction': 'rtl' }],                         // text direction

        [{ 'header': [1, 2, 3, 4, 5, 6, false] }],
      
        [{ 'color': [] }, { 'background': [] }],          // dropdown with defaults from theme
        [{ 'align': [] }],
      
        ['clean']        
        ]
    },
    placeholder: 'Write something...',
    theme: 'snow'
    });
var content = "";
function submitContent() {
    content = quill.root.innerHTML;
    $('#content-container').hide();
    $('#form-container').fadeIn();
}
function preview() {
    $('#form-container').fadeOut();
    $('#preview-content').html(content);
    $('#preview-container').fadeIn();
}
function back() {
    $('#form-container').hide();
    $('#preview-container').hide();
    // quill.setContents({
    //     "ops":[
    //         {"insert":content}
    //     ]
    // });
    quill.root.innerHTML = content;
    $('#content-container').fadeIn();
}
function postBlog(){
    //var form = document.querySelector('form');
    //var content = document.querySelector('input[name=content]');
    //var content = quill.root.innerHTML;
    //alert(content);
    //var temp = quill.getContents();
    //alert(JSON.stringify(temp));
    //console.log(text);
    //console.log("Submitted", $(form).serialize(), $(form).serializeArray());
    var path = $('#id_file').val();
    // console.log(path);
    path = path.replace(/^.*[\\\/]/, '')
    path = generateNewFileName(path);
    var link = encodeURIComponent(path);
    // console.log(link);
    var title = $('#id_title').val();
    var provider = $('#provider_selector option:selected').val();
    var category = $('#category_selector option:selected').val();
    var request = $.ajax({
        url: "/apis/post",
        method: "POST",
        contentType: "application/json",
        dataType: "json",
        data: JSON.stringify({
            "blog_content": content,
            "blog": {
                "img_url": link,
                "title": title,
                "provider": provider,
                "category": category,
                "tags": tagList
            }
        }),
    }).done(function() {
        window.location.href = "/";
        return false;
    });
    // No back end to actually submit to!
}
var tagList = [];
var tagMapping = {};
function updateTag(tagID,tagName){
    tagMapping[tagID] = tagName;
    if (tagList.includes(tagID)){
        var index = tagList.indexOf(tagID);
        tagList.splice(index,1);
    }else{
        tagList.push(tagID);
    }
    $('#selected-tag').empty();
    tagList.forEach(function(id){
        $('#selected-tag').append('<i class="fa fa-tags"> ' + tagMapping[id] + '</i> &nbsp');
    });
}
$(document).ready(function(){
    $('#form-container').hide();
    $('#preview-container').hide();
    $('.tag').click(function(){
        var isSelcted = $(this).hasClass('tag-selected');
        $(this).toggleClass('tag-selected');
        var id = $(this).data('id');
        var name = $(this).data('name');
        updateTag(id,name);
    });
});

