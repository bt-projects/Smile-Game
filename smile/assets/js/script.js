
// JQUERY
$(document).ready(function(){
    setTimeout(function() {
        if($('#msg').length > 0) {
            console.log(msg.length);
            $('#msg').remove();
        } else {
            $('#img').hide();
        }
    }, 3000)
})

//