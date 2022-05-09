function changeMajor(thing) 
{
	console.log('changed')
	var formData = {
        maj : thing.value
      };
      console.log(formData)
      $.post("/changeMajor", formData, function(data)
      {
          console.log(data)
      }
      )
};