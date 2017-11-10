$(document).ready(function(){
    $('.likes').click(function(){
        var url = $(this).attr('datasrc');
        var id = $(this).attr('data-key');
        $.ajax({
            url: url,
            success: function (result) {
                if (result.errors) {
                    console.log("errors = ", errors);
                } else {
                    $('#like_count_' + id).html(result);
                }
            }
        })
    })
});
