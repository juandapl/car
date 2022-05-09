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
        location.assign('/fyp')
    }
    )
}

function removeCourse(thing)
{
    console.log("click")
    var regNumber = thing.parentElement.querySelector("#in").textContent
    
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

function generate()
{
    console.log("click")

    var request = {
        text: "cmon do it"
    }
        console.log(request)
    $.post("/generateFYP", request, function(data)
    {
        console.log(data)
        location.reload()
    }
    )
}