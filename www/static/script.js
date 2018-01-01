$(document).ready(function(){
	$('.sliders').responsiveSlides({
		nav: true,
		pager: true,
		speed: 800,
		timeout: 5000
	});

	$('.ui.sticky').sticky({
		context: 'body'
	});
});