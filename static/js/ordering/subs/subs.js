
$("document").ready(function(){
    if($("#id_condiments").hide()){
        $("#id_condiments input:checkbox").prop("checked", false);
    }
    if($("select[name='subs_type']") == "Steak and Cheese"){
        $("#id_condiments").show();
    }
    $("select[name='subs_type']").change(function(){
        if($(this).val() == "Steak and Cheese"){
            $("#id_condiments").show();
        } else{
            $("#id_condiments input:checkbox").prop("checked", false);
            $("#id_condiments").hide();
        }
    })
    
    $("#id_condiments input[value='none']").change(function(){
        if($(this).is(":checked")){
            $("#id_condiments input").not(this).prop("checked", false);
            $("#id_condiments input").not(this).prop("disabled", true);
        } else{
            $("#id_condiments input").not(this).prop("disabled", false);
        }
    })
    $("#get_subs_price").click(function(){
        let condiments = [];
        $("#id_condiments input:checkbox:checked").each(function(){
            condiments.push($(this).val());
        })
        $.ajax({
            method: 'get',
            url:'/get_subs_price/',
            data : {
                "subs_size": $("select[name='subs_size']").val(),
                "subs_type": $("select[name='subs_type']").val(),
                "condiments": condiments,
                "extra_cheese": $("input[name='extra_cheese']").prop("checked")     
            }
        }).done(function(data){
            if(data.header){
                $("#price").text(data.message)
            }else{
                $("#price").text(data.price)
            }
        })
    })
})
