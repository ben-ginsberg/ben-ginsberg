jQuery(document).ready(function ($) {

	imageRadio = 1.6;
	winowMinWidth = 1060;
	
	jQuery.fn.addBgImage=function () {
		$('.slide').css('background-image', 'none');
		$('.ie-img').css('display', 'block');
		$.setImageSize();
	}

	$(window).resize(function(){
		$.setImageSize();
	});
	$.extend({setImageSize:function(){
		var currentWidth = $(window).width();
		var currentHeight = $(window).height();
		var windowRadio = $(window).width()/$(window).height();
		if (windowRadio >= imageRadio) {
			$('.ie-img').css('width', currentWidth);
			var imgHeight = currentWidth / imageRadio;
			var imgOffsetY = (parseInt(imgHeight) - currentHeight)/2;
			$('.ie-img').css('top', -imgOffsetY);
		}
		else {
			if (currentWidth < windowMinWidth){
				$('.ie-img').css('height', currentHeight);
			}
		}
	}});
	$(window).addBgImage();

});
