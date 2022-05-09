$('#try5').click(function()
{
    var formData = {
        email : $("#email").val(),
        password : $("#password").val()
      };
      

      $.post("/login", formData, function(data)
      {
          console.log(data)
          location.reload()
      }
      )
});