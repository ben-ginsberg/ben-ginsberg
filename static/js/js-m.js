jQuery(document).ready(function ($) {


$(function(){
	var currentId = $('body').attr("id");
	switch (currentId) {
		case 'about-m': {
			$('#nav2').addClass('active-bg');
			$('#nav2 a').removeAttr('href');
			$('#nav2 a').css('cursor', 'default');
		};
		break;
		case 'privacy-m': {
	alert('dfd');
			$('#nav3').addClass('active-bg');
			$('#nav3 a').removeAttr('href');
			$('#nav3 a').css('cursor', 'default');
		}
		break;
		case 'terms-m': {
			$('#nav4').addClass('active-bg');
			$('#nav4 a').removeAttr('href');
			$('#nav4 a').css('cursor', 'default');
		}
		break;
	}
})


});
