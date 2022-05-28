$(document).ready(function(){
    $.ajax('https://fourtonfish.com/hellosalut/?lang=fr',
    {
        success: function (data) {
        $('#hello').append(data.hello);
        }

    });
})
