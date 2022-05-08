$('#add').click(function()
{
    var regNumber = $(this).parent().parent().find("#reg").val()
    var request = {
        reg: regNumber,
        year: $("#year").val(),
        sem: $("#sem").val()
    }
    $.post("/addCourse", request)
})