function addMajor(thing)
{
    console.log("adding major")
    var MajorName = thing.parentElement.querySelector("#newMajorName").value
    
    var request = {
        name : MajorName
    }
        console.log(request)
    $.post("/addMajor", request, function(data)
    {
        console.log(data)
        location.reload(); 
    }
    )
}

function addReq(thing)
{
    console.log("adding major")
    var ClassName = thing.parentElement.querySelector("#newRequirement").value
    var MajorName = thing.parentElement.parentElement.querySelector("#th4").textContent
    
    
    console.log(MajorName)


    var request = {
        name : ClassName,
        major : MajorName
    }
        console.log(request)
    $.post("/addClass", request, function(data)
    {
        console.log(data)
        location.reload(); 
    }
    )
}

function addPreReq(thing)
{
    console.log("adding major")
    var PreReqName = thing.parentElement.querySelector("#newPreReq").value
    var ClassName = thing.parentElement.parentElement.querySelector("#td4").textContent
    var MajorName = thing.parentElement.parentElement.parentElement.querySelector("#th4").textContent


    var request = {
        name : PreReqName,
        class: ClassName,
        major : MajorName
    }
        console.log(request)
    $.post("/addPreReq", request, function(data)
    {
        console.log(data)
        location.reload(); 
    }
    )
}


function deleteReq(thing)
{
    console.log("deleting major")
    var ClassName = thing.parentElement.parentElement.querySelector("#td4").textContent
    var MajorName = thing.parentElement.parentElement.parentElement.querySelector("#th4").textContent

    var request = {
        name : ClassName,
        major : MajorName
    }
        console.log(request)
    $.post("/deleteReq", request, function(data)
    {
        console.log(data)
        location.reload(); 
    }
    )
}


