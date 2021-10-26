$("#selEsp").change(function(){

    console.log($(this).find(":selected").val());
    if ($(this).find(":selected").val() != "")
        {
            $("#selMed").prop('disabled', false);
        }
    else{
        $("#selMed").prop('disabled', true);
        $("#selDia").prop('disabled', true);
        $("#selHor").prop('disabled', true);
        $("#reservar").prop('disabled', true);

        $('#selMed option:eq("")').prop('selected', true);
        $('#selDia option:eq("")').prop('selected', true);
        $('#selHor option:eq("")').prop('selected', true);
    }
});

$("#selMed").change(function(){

    if ($(this).find(":selected").val() != "")
        {
            $("#selDia").prop('disabled', false);
        }
    else{
        $("#selDia").prop('disabled', true);
        $("#selHor").prop('disabled', true);
        $("#reservar").prop('disabled', true);

        $('#selDia option:eq("")').prop('selected', true);
        $('#selHor option:eq("")').prop('selected', true);
    }
});

$("#selDia").change(function(){

    if ($(this).find(":selected").val() != "")
        {
            $("#selHor").prop('disabled', false);
        }
    else{
        $("#selHor").prop('disabled', true);
        $("#reservar").prop('disabled', true);

        $('#selHor option:eq("")').prop('selected', true);
    }
});

$("#selHor").change(function(){

    if ($(this).find(":selected").val() != "")
        {
            $("#reservar").prop('disabled', false);
        }
    else{
        $("#reservar").prop('disabled', true);
    }
});