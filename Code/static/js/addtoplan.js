function addCourse(thing)
{
    console.log("click")
    var regNumber = thing.parentElement.parentElement.querySelector("#reg").textContent
    
    var request = {
        reg: regNumber,
        year: $("#year").val(),
        sem: $("#sem").val()


    }
        console.log(request)
    $.post("/addCourse", request, function(data)
    {
        console.log(data)
    }
    )
}   