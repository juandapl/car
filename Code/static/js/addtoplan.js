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

function removeCourse(thing)
{
    console.log("click")
    var regNumber = thing.parentElement.querySelector("#info").textContent
    
    var request = {
        reg: regNumber
    }
        console.log(request)
    $.post("/removeCourse", request, function(data)
    {
        console.log(data)
        location.reload()
    }
    )
}   