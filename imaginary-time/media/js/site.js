;(function($){
var site = window.site = new function() {
    this.csrvToken;
    
	this.init = function() 
	{
	    var self = this;
        
        this.formPlaceholders();
        this.responseForm();
        this.debug();
    };

    this.debug = function()
    {
        
    };

    this.responseForm = function()
    {
        var self = this;

    	
    	$('#feedbackForm').submit(function(e)
    	{
    	    e.preventDefault();
    	    
            var data = $(this).serialize();
            Dajaxice.futures.submit_feedback(self.feedback_callback, {'form':data});
    	});
	};
	

	this.feedback_callback = function(data)
	{
	    // reset error fields
	    $('#feedbackForm input, #feedbackForm textarea').removeClass('error');
	    
        if (data.success == true)
        {
            // 1. fade out form

            $('#feedbackForm').fadeOut(300, function() 
            {
                // 2. fade in success message
                $('#feedbackCheck').fadeIn(300, function() 
                {
                    // 3. wait 1000 ms
                    setTimeout(function() 
                    {
                        // 4. animate form back to its original position
                        $('#feedback').animate(
                	        {
                	            right: -322
                	        }, 1000, function() 
                	            {
                	                // 5. restore the form's original state
                	                $('#feedbackCheck').hide();
                	                $('#feedbackForm input, #feedbackForm textarea').not('.formSubmit').val('');
                	                $('#feedbackForm').show();                                        
                	            }
                	    );
                    }, 1000);
                });
            });
        }
        else
        {
            for (field in data.errors)
            {
                $('#id_' + field).addClass('error');
            }
        }
	};
	
	
	this.formPlaceholders = function()
	{
        var arrInputs = document.getElementsByTagName("input");
        for (var i = 0; i < arrInputs.length; i++) 
        {
            var curInput = arrInputs[i];
            if (!curInput.type || curInput.type == "" || curInput.type == "text")
            self.handlePlaceholder(curInput);
        }	
        
        var arrTextareas = document.getElementsByTagName("textarea");
        for (var i = 0; i < arrTextareas.length; i++) 
        {
            var curTextarea = arrTextareas[i];
            self.handlePlaceholder(curTextarea);
        }	    
	};
	
    this.handlePlaceholder = function(oTextbox)
    {
        if (typeof oTextbox.placeholder == "undefined")
        {
            var curPlaceholder = oTextbox.getAttribute("placeholder");
            
            if (curPlaceholder && curPlaceholder.length > 0)
            {
                oTextbox.value = curPlaceholder;
                oTextbox.setAttribute("old_color", oTextbox.style.color);
                oTextbox.style.color = "#005fff";
                oTextbox.onfocus = function()
                {
                    this.style.color = this.getAttribute("old_color");
                    if (this.value === curPlaceholder)
                        this.value = "";
                };
                oTextbox.onblur = function()
                {
                    if (this.value === "")
                    {
                        this.style.color = "#005fff";
                        this.value = curPlaceholder;
                    }
                };
            }
        }
    }	

	this.appendFormError = function(form, message)
	{
        $('.errors', form).append('<p>' + message + '</p>');		    
	};
	
	this.outputError = function(message)
	{
        $('#error #errorMessage').html('<p>' + message + '</p>');
        $('#error').fadeIn(1000);	    
	};
};
})(jQuery);

$(document).ready(function(){
	site.init();
});		