$(document).ready(function() {
    // var quill = new Quill('#content');
    // $('#content').html(quill.root.innerHTML);
    // var delta = quill.root.innerHTML;
    var content = $('#content').val();
    alert(content);
    //var html = $.parseHTML(content);
    $('#demo').append(content);
})