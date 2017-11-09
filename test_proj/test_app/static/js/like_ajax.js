$(document).ready(function(){
    $('.likes').click(function(){
        var url = $(this).attr('datasrc');
        $.ajax({
            url: url,
            success: function (result) {
                if (result.errors) {
                    console.log("errors = ", errors);
                } else {
                    $('.like_count').html(result);
                }
            }
        })
    })
});
