(function($) {

    $(".toggle-password").click(function() {

        $(this).toggleClass("zmdi-eye zmdi-eye-off");
        var input = $($(this).attr("toggle"));
        if (input.attr("type") == "password") {
          input.attr("type", "text");
        } else {
          input.attr("type", "password");
        }
      });

})(jQuery);

var form_fields = document.getElementsByTagName('input')
		form_fields[1].placeholder='First Name..';
    form_fields[2].placeholder='Last Name..';
    form_fields[3].placeholder='Userame..';
		form_fields[4].placeholder='Email..';
		form_fields[5].placeholder='Enter password...';
		form_fields[6].placeholder='Re-enter Password...';
    form_fields[7].placeholder='Phone Number...';


		for (var field in form_fields){	
			form_fields[field].className += ' form-control'
		}