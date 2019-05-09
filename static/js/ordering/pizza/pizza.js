$("select[name='type']").change(function(){
    if($(this).val() == "one topping"){
        $("#id_toppings_1").show();
        $("#id_toppings_2").hide();
        $("#id_toppings_2 option:selected").prop("selected", false);
        $("#id_toppings_3").hide();
        $("#id_toppings_3 option:selected").prop("selected", false);
    }else if($(this).val() == "two toppings"){
        $("#id_toppings_1").show();
        $("#id_toppings_2").show();
        $("#id_toppings_3").hide();
    }else if($(this).val() == "three toppings"){
        $("#id_toppings_1").show();
        $("#id_toppings_2").show();
        $("#id_toppings_3").show();
    }else{
        $("#id_toppings_1").hide();
        $("#id_toppings_2").hide();
        $("#id_toppings_3").hide();
    }
})

$("#get_pizza_price").click(function(){
    $.ajax({
        method: 'get',
        url:'/get_pizza_price/',
        data : {
            "base": $("select[name='base']").val(),
            "size": $("select[name='size']").val(),
            "type": $("select[name='type']").val()          
        }
    }).done(function(data){
        if(data.header){
            $("#price").text(data.message)
        }else{
            $("#price").text(data.price)
        }
    })
})