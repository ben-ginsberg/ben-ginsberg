jQuery(document).ready(function ($) {
	narrowWith = 1200;
	currentId = $('body').attr("id");

//Top Nav=================
	switch (currentId) {
		case 'about': {
			$('#nav2').addClass('nav-active');
			$('#nav2 a').removeAttr('href');
			$('#nav2 a').css('cursor', 'default');
		};
		break;
		case 'privacy': {
			$('#nav3').addClass('nav-active');
			$('#nav3 a').removeAttr('href');
			$('#nav3 a').css('cursor', 'default');
		}
		break;
		case 'terms': {
			$('#nav4').addClass('nav-active');
			$('#nav4 a').removeAttr('href');
			$('#nav4 a').css('cursor', 'default');
		}
		break;
	}


//narrow or normal window style=================
$("body").ready(function(){

	if ($(document.body).width() < narrowWith) {
		$(this).setNarrow();
		return false;
	}
	else {
		$(this).setNormal();
		return false;
	}
});
$(window).resize(function(){
	if ($(document.body).width() < narrowWith) {
		$(this).setNarrow();
		return false;
	}
	else {
		$(this).setNormal();
		return false;
	}
	
});
jQuery.fn.setNarrow=function () {
		$('.left-side').css('display', 'none');
		$('.right-side').css('margin-left', '0');
		$('.footer-get-social').css('display', 'block');
}
jQuery.fn.setNormal=function () {
		$('.left-side').css('display', 'block');
		$('.right-side').css('margin-left', '320px');
		$('.footer-get-social').css('display', 'none');
}


});
