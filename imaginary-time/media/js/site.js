;(function($){
var site = window.site = new function() {
    this.csrvToken;
    
	this.init = function() 
	{
	    var self = this;
        
        this.sliders();
        this.responseForm();
        this.debug();
    };

    this.debug = function()
    {
        
    };
    
    this.sliders = function()
    {
        var self = this;
        
        var sliders = $('.sliderContainer');
        
        $('.sliderContainer').click(function(e)
        {
            var container = $(this).parent();
            var previousValue = self.calculateValueFromElement(this);
            var newValue = self.calculateValueFromClick(e, this, container);
            $('input', container).val(newValue);
            
            var diff = newValue - previousValue;
            var i=0;
                        
            while(diff > 0)
            {
                if ($(this)[0] != $(sliders)[i])
                {
                    var slider = sliders.eq(i);
                    var container = $(slider).parent();
                    var previousSliderValue = self.calculateValueFromElement(slider);
                    if (previousSliderValue > 0)
                    {
                        var newSliderValue = previousSliderValue - 1;
                        $('input', container).val(newSliderValue);
                        diff -= 1;                        
                    }
                }
                i++;
                if (i == 12) { i = 0; }
            }
            
            while(diff < 0)
            {
                if ($(this)[0] != $(sliders)[i])
                {
                    var slider = sliders.eq(i);
                    var container = $(slider).parent();
                    var previousSliderValue = self.calculateValueFromElement(slider);
                    if (previousSliderValue > 0)
                    {
                        var newSliderValue = previousSliderValue + 1;
                        $('input', container).val(newSliderValue);
                        diff += 1;                        
                    }
                }
                i++;
                if (i == 12) { i = 0; }
            }
            
            for(var i=0; i<sliders.size(); i++)
            {
                var slider = sliders.eq(i);
                var container = $(slider).parent();

                var value = self.calculateValueFromElement(slider);
                var fillPercentage = self.map(value, 0.0, 12.0, 0, 100);

                $('.fill', slider).css({'height': fillPercentage+'%'});
                $('.value', container).html(Math.round(value));
                $('input', container).val(value);
            }
        });
    };
    
    this.calculateValueFromClick = function(event, element, container)
    {
        var self = this;
        
        var elementPosition = $(element).offset().top;
        var clickPosition = event.pageY;
        var click = (clickPosition - elementPosition);
        
        return parseFloat(Math.round(self.map(click, 0, 240, 12.0, 0.0)));
    };
    
    this.calculateValueFromElement = function(element)
    {
        var self = this;
        
        var container = $(element).parent();
        return parseFloat($('input', container).val());
        
    };    

    this.responseForm = function()
    {
        var self = this;

    	
    	$('#timeForm').submit(function(e)
    	{
    	    e.preventDefault();
    	    
            var data = $(this).serialize();
            Dajaxice.imaginary_time.submit_form(self.form_callback, {'form':data});
    	});
	};
	

	this.form_callback = function(data)
	{
        if (data.success == true)
        {
            // 1. fade out form

            $('.formSubmit').fadeOut(100, function() 
            {
                // 2. fade in success message
                $('.success').fadeIn(300, function() 
                {
                    // 3. wait 500 ms
                    setTimeout(function() 
                    {
                        // 4. animate form back to its original position
                        $('#formContent').animate(
                	        {
                	            left: 2000
                	        }, 2500, function() 
                	            {
                	                // 5. restore the form's original state
                	                $('.success').fadeOut(1000, function()
                	                {
                	                    $('.fill').css({'height':'12.5%'});
                	                    $('input').not('.formSubmit').val(2.0);
                	                    $('#formContent').css({'left':'0'}).fadeIn(500, function()
                	                    {
                                            $('.formSubmit').fadeIn(200);
                	                    });
                    	                
                	                });
                	            }
                	    );
                    }, 500);
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

	this.appendFormError = function(form, message)
	{
        $('.errors', form).append('<p>' + message + '</p>');		    
	};
	
	this.outputError = function(message)
	{
        $('#error #errorMessage').html('<p>' + message + '</p>');
        $('#error').fadeIn(1000);	    
	};
	
	this.roundToHalf = function(value)
	{ 
       var converted = parseFloat(value); // Make sure we have a number 
       var decimal = (converted - parseInt(converted, 10)); 
    
       decimal = Math.round(decimal * 10); 
    
       if (decimal == 5) { return (parseInt(converted, 10)+0.5); } 
    
       if ( (decimal < 3) || (decimal > 7) ) { 
          return Math.round(converted); 
       } else {
          return (parseInt(converted, 10)+0.5); 
       } 
    }
	
    this.map = function(value, istart, istop, ostart, ostop, confine) 
    {
       var result = ostart + (ostop - ostart) * ((value - istart) / (istop - istart));
       if (confine)
       {
           result = (result > ostop) ? ostop : result;
           result = (result < ostart) ? ostart : result;
       }
       return result;
    };	
};
})(jQuery);

$(document).ready(function(){
	site.init();
});		