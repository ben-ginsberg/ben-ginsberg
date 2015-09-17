jQuery(document).ready(function ($) {


	//initialise Stellar.js
	$(window).stellar();

	//Cache some variables
	slide = $('.slide');
	button = $('.button');
	mywindow = $(window);
	htmlbody = $('html,body');


//content fadein/fadeout=================
$('.fade-item').waypoint(function(direction) {
	if (direction === 'up') {
		$(this).css('opacity', 1);
	}
	else {
		$(this).css('opacity', 0);
	}
}, { offset: '10%' });
$('.fade-item').waypoint(function(direction) {
	if (direction === 'down') {
		$(this).css('opacity', 1);
	}
	else {
		$(this).css('opacity', 0);
	}
}, { offset: '90%' });
$('.fade-image').waypoint(function(direction) {
	if (direction === 'up') {
		$(this).css('opacity', 1);
	}
	else {
		$(this).css('opacity', 0);
	}
}, { offset: '-10%' });
$('.fade-image').waypoint(function(direction) {
	if (direction === 'down') {
		$(this).css('opacity', 1);
	}
	else {
		$(this).css('opacity', 0);
	}
}, { offset: '70%' });

/*
$('.download-l').click(function(){
	$(this).fadeOut(50, function(){
		$('#send-link').fadeIn(100);
	});
});
*/

    //Create a function that will be passed a slide number and then will scroll to that slide using jquerys animate. The Jquery
    //easing plugin is also used, so we passed in the easing method of 'easeInOutQuint' which is available throught the plugin.
    function goToByScroll(dataslide) {
        htmlbody.animate({
            scrollTop: $('.slide[data-slide="' + dataslide + '"]').offset().top
        }, 1000, 'easeOutExpo');
    }



    //When the user clicks on the button, get the get the data-slide attribute value of the button and pass that variable to the goToByScroll function
    button.click(function (e) {
        e.preventDefault();
        dataslide = $(this).attr('data-slide');
        goToByScroll(dataslide);

    });


});
