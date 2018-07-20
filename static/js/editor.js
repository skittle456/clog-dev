
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
function postBlog(){
    //var form = document.querySelector('form');
    //var content = document.querySelector('input[name=content]');
    var content = quill.root.innerHTML;
    //alert(content);
    //var temp = quill.getContents();
    //alert(JSON.stringify(temp));
    //console.log(text);
    //console.log("Submitted", $(form).serialize(), $(form).serializeArray());
    var path = $('#id_file').val();
    path = path.replace(/^.*[\\\/]/, '')
    var link = encodeURIComponent(path);
    console.log(link);
    var request = $.ajax({
        url: "/apis/post",
        method: "POST",
        contentType: "application/json",
        dataType: "json",
        data: JSON.stringify({
            "blog_content":content,
            "blog":{
                "img_url":link,
                "title": $('#id_title').val(),
                "provider":$('#id_provider').val(),
                "category":$('#id_category').val(),
                "tags":$('#id_tags').val()
            }
        }),
    }).done(function(){
        location.href = "/"
    })
    // No back end to actually submit to!
    //alert('Open the console to see the submit data!')
    return false;
}