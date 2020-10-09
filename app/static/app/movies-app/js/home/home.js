// Set Up BIG Swiper
let homeHeaderSwiper = new Swiper('#home-slider', {
	pagination: {
		el: '.home-slider-pagination',
		clickable: true,
	},
	navigation: {
		nextEl: '.home-slide-next',
		prevEl: '.home-slide-prev',
	},
});

// LATEST MOVIES AN SERIES SLIDERS
let options = {
	slidesPerView: 5,
	spaceBetween: 0,
	freeMode: true,
	init: true,
	breakpoints: {
		640: {
			slidesPerView: 2,
			spaceBetween: 20,
		},
		768: {
			slidesPerView: 4,
			spaceBetween: 40,
		},
		1024: {
			slidesPerView: 6,
			spaceBetween: 50,
		}
	},
}

let homeLatestMoviesSwiper = new Swiper('.latest-movies--wrapper', options);
let homeLatestSeriesSwiper = new Swiper('.latest-series--wrapper', options);

// var xhttp = new XMLHttpRequest();
// xhttp.onreadystatechange = function() {
//     if (this.readyState == 4 && this.status == 200) {
//       console.log(xhttp.response)
//     }
// };
// xhttp.open("GET", "http://localhost:8000/", true);xhttp.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
// xhttp.send();