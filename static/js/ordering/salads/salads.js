$("#get_salads_price").click(function(){
    $.ajax({
        method: 'get',
        url:'/get_salads_price/',
        data : {
            "salads_type": $("select[name='salads_type']").val()          
        }
    }).done(function(data){
        if(data.header){
            $("#price").text(data.message)
        }else{
            $("#price").text(data.price)
        }
    })
})