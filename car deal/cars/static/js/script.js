$(document).ready(function () {
	$('.slider').slick({
		centerPadding: '60px',
		autoplay: true,
		arrows: false,
		responsive: [
			{
				breakpoint: 1024,
				settings: {
					slidesToShow: 2,
					slidesToScroll: 1,
				},
			},
			{
				breakpoint: 800,
				settings: {
					slidesToShow: 1,
					slidesToScroll: 1,
				},
			},
		],
	});
});
$(document).ready(function () {
	$('.top').slick({
		dots: false,
		infinite: true,
		speed: 200,
		slidesToShow: 1,
		autoplay: true,
		arrows: true,
		cssEase: 'linear',
	});
});

$('.car-left ').click(function () {
	$('.slider').slick('slickPrev');
});

$('.car-right').click(function () {
	$('.slider').slick('slickNext');
});


