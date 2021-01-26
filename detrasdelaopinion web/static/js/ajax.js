$(document).ready(function(){

    const mail = () => {
        
        $.ajax({
            type: "POST",
            url:'/ajax_post',
            data: $('form').serialize(),
            success: function(response){
                console.log(response);
            },
            error:function(error){
                console.log("Error");
            }
        })
    }

    $('#email-form').submit(function(e){
        // e.eventDefault()
        mail();
    })

});