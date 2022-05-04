
$('#submit').click(function()
{
    var formData = {
        year: $("#year").val(),
        sem: $("#sem").val(),
        department: $("#department").val(),
        query: $("#query").val(),
      };
      console.log(formData)
      $.post("/coursesearchresults", formData, function(data)
      {
          $("#search_results").html(data)
      }
      )
});

