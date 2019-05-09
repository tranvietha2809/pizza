$("#get_platters_price").click(function(){
    $.ajax({
        method: 'get',
        url:'/get_platters_price/',
        data : {
            "platters_size": $("select[name='platters_size']").val(),
            "platters_type": $("select[name='platters_type']").val()          
        }
    }).done(function(data){
        if(data.header){
            $("#price").text(data.message)
        }else{
            $("#price").text(data.price)
        }
    })
})