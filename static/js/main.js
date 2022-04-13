$(document).ready(function(){
    function ajax_login(){
        $.ajax({
            url: '/ajax-login',
            data: $('form').serialize(),
            type: 'POST',
            success: function(res){
                console.log(res);
            },        
            error: function(res){
                console.log(res);
            }
        });
    }
    $('#loginForm').submit(function(e){
        e.preventDefault();
        ajax_login();
    });
});