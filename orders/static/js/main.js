 AOS.init({
 	duration: 800,
 	easing: 'slide'
 });

(function($) {

	"use strict";

	$(window).stellar({
    responsive: true,
    parallaxBackgrounds: true,
    parallaxElements: true,
    horizontalScrolling: false,
    hideDistantElements: false,
    scrollProperty: 'scroll',
    horizontalOffset: 0,
	  verticalOffset: 0
  });

  // Scrollax
  $.Scrollax();


	var fullHeight = function() {

		$('.js-fullheight').css('height', $(window).height());
		$(window).resize(function(){
			$('.js-fullheight').css('height', $(window).height());
		});

	};
	fullHeight();

	// loader
	var loader = function() {
		setTimeout(function() {
			if($('#ftco-loader').length > 0) {
				$('#ftco-loader').removeClass('show');
			}
		}, 1);
	};
	loader();

	// Scrollax
   $.Scrollax();

	var carousel = function() {
		$('.home-slider').owlCarousel({
	    loop:true,
	    autoplay: true,
	    margin:0,
	    animateOut: 'fadeOut',
	    animateIn: 'fadeIn',
	    nav:false,
	    autoplayHoverPause: false,
	    items: 1,
	    navText : ["<span class='ion-md-arrow-back'></span>","<span class='ion-chevron-right'></span>"],
	    responsive:{
	      0:{
	        items:1,
	        nav:false
	      },
	      600:{
	        items:1,
	        nav:false
	      },
	      1000:{
	        items:1,
	        nav:false
	      }
	    }
		});
		$('.carousel-work').owlCarousel({
			autoplay: true,
			center: true,
			loop: true,
			items:1,
			margin: 30,
			stagePadding:0,
			nav: true,
			navText: ['<span class="ion-ios-arrow-back">', '<span class="ion-ios-arrow-forward">'],
			responsive:{
				0:{
					items: 1,
					stagePadding: 0
				},
				600:{
					items: 2,
					stagePadding: 50
				},
				1000:{
					items: 3,
					stagePadding: 100
				}
			}
		});

	};
	carousel();

	$('nav .dropdown').hover(function(){
		var $this = $(this);
		// 	 timer;
		// clearTimeout(timer);
		$this.addClass('show');
		$this.find('> a').attr('aria-expanded', true);
		// $this.find('.dropdown-menu').addClass('animated-fast fadeInUp show');
		$this.find('.dropdown-menu').addClass('show');
	}, function(){
		var $this = $(this);
			// timer;
		// timer = setTimeout(function(){
			$this.removeClass('show');
			$this.find('> a').attr('aria-expanded', false);
			// $this.find('.dropdown-menu').removeClass('animated-fast fadeInUp show');
			$this.find('.dropdown-menu').removeClass('show');
		// }, 100);
	});


	$('#dropdown04').on('show.bs.dropdown', function () {
	  console.log('show');
	});

	// scroll
	var scrollWindow = function() {
		$(window).scroll(function(){
			var $w = $(this),
					st = $w.scrollTop(),
					navbar = $('.ftco_navbar'),
					sd = $('.js-scroll-wrap');

			if (st > 150) {
				if ( !navbar.hasClass('scrolled') ) {
					navbar.addClass('scrolled');
				}
			}
			if (st < 150) {
				if ( navbar.hasClass('scrolled') ) {
					navbar.removeClass('scrolled sleep');
				}
			}
			if ( st > 350 ) {
				if ( !navbar.hasClass('awake') ) {
					navbar.addClass('awake');
				}

				if(sd.length > 0) {
					sd.addClass('sleep');
				}
			}
			if ( st < 350 ) {
				if ( navbar.hasClass('awake') ) {
					navbar.removeClass('awake');
					navbar.addClass('sleep');
				}
				if(sd.length > 0) {
					sd.removeClass('sleep');
				}
			}
		});
	};
	scrollWindow();


	var counter = function() {

		$('#section-counter').waypoint( function( direction ) {

			if( direction === 'down' && !$(this.element).hasClass('ftco-animated') ) {

				var comma_separator_number_step = $.animateNumber.numberStepFactories.separator(',')
				$('.number').each(function(){
					var $this = $(this),
						num = $this.data('number');
						console.log(num);
					$this.animateNumber(
					  {
					    number: num,
					    numberStep: comma_separator_number_step
					  }, 7000
					);
				});

			}

		} , { offset: '95%' } );

	}
	counter();

	var contentWayPoint = function() {
		var i = 0;
		$('.ftco-animate').waypoint( function( direction ) {

			if( direction === 'down' && !$(this.element).hasClass('ftco-animated') ) {

				i++;

				$(this.element).addClass('item-animate');
				setTimeout(function(){

					$('body .ftco-animate.item-animate').each(function(k){
						var el = $(this);
						setTimeout( function () {
							var effect = el.data('animate-effect');
							if ( effect === 'fadeIn') {
								el.addClass('fadeIn ftco-animated');
							} else if ( effect === 'fadeInLeft') {
								el.addClass('fadeInLeft ftco-animated');
							} else if ( effect === 'fadeInRight') {
								el.addClass('fadeInRight ftco-animated');
							} else {
								el.addClass('fadeInUp ftco-animated');
							}
							el.removeClass('item-animate');
						},  k * 50, 'easeInOutExpo' );
					});

				}, 100);

			}

		} , { offset: '95%' } );
	};
	contentWayPoint();


	// navigation
	var OnePageNav = function() {
		$(".smoothscroll[href^='#'], #ftco-nav ul li a[href^='#']").on('click', function(e) {
		 	e.preventDefault();

		 	var hash = this.hash,
		 			navToggler = $('.navbar-toggler');
		 	$('html, body').animate({
		    scrollTop: $(hash).offset().top
		  }, 700, 'easeInOutExpo', function(){
		    window.location.hash = hash;
		  });


		  if ( navToggler.is(':visible') ) {
		  	navToggler.click();
		  }
		});
		$('body').on('activate.bs.scrollspy', function () {
		  console.log('nice');
		})
	};
	OnePageNav();


	// magnific popup
	$('.image-popup').magnificPopup({
    type: 'image',
    closeOnContentClick: true,
    closeBtnInside: true,
    fixedContentPos: true,
    mainClass: 'mfp-no-margins mfp-with-zoom', // class to remove default margin from left and right side
     gallery: {
      enabled: true,
      navigateByImgClick: true,
      preload: [0,1] // Will preload 0 - before current, and 1 after the current image
    },
    image: {
      verticalFit: true
    },
    zoom: {
      enabled: true,
      duration: 300 // don't foget to change the duration also in CSS
    }
  });

  $('.popup-youtube, .popup-vimeo, .popup-gmaps').magnificPopup({
    disableOn: 700,
    type: 'iframe',
    mainClass: 'mfp-fade',
    removalDelay: 160,
    preloader: false,

    fixedContentPos: false
  });


  $('#appointment_date').datepicker({
	  'format': 'm/d/yyyy',
	  'autoclose': true
	});

	$('#appointment_time').timepicker();




})(jQuery);


document.addEventListener("DOMContentLoaded", () => {

  // document.querySelector("#").
  document.getElementById("v-pills-tab").firstElementChild.className = "nav-link active";
  document.getElementById("v-pills-tabContent").firstElementChild.className = "tab-pane fade show active";

});

 // id =  v-pills-tab


var csrftoken = getCookie('csrftoken');

function add2mycart(item_id) {

  console.log(item_id);
  toAdd = [];
  var item = {
    "id" : item_id,
  }
  toAdd.push(item);

  console.log(toAdd.length);

  const data = new FormData();
  data.append('csrfmiddlewaretoken', csrftoken);
  data.append('items', JSON.stringify(toAdd));

  // ajax request
  const request = new XMLHttpRequest();
  request.open('POST', '/add2chart');
  request.send(data);


  // After request completes
  request.onload = () => {
      const data = JSON.parse(request.responseText);
      if (data.success)
          alert(`Added item(s) to shopping cart!`)
  };

  // prevernt reload
  return false;
};


function changeTotal(data, element) {
  // console.log(data);
/*
  Data Example:
    {data{
      item_id: 6
      quantity: "4"
      subtotal: 33
      total:
        subtotal__sum: 85
        __proto__: Object
        __proto__: Object
      }
    success: true
    __proto__: Object}
*/

  total = data.data.total.subtotal__sum;
  element.parentElement.parentElement.parentElement.children[2].innerHTML = "$"+data.data.price;
  element.parentElement.parentElement.nextElementSibling.nextElementSibling.nextElementSibling.innerHTML = "$"+data.data.subtotal;
  // element.parentElement.parentElement.parentElement.innerHTML = data.price;

  document.querySelector("#total").innerHTML = total;
};


function changePrice(element, item_id){
    newPrice = element.value
    price = [];
    var item = {
      "id" : item_id,
      "newPrice" : newPrice,
    };
    price.push(item);

    const data = new FormData();
    data.append('csrfmiddlewaretoken', csrftoken);
    data.append('items', JSON.stringify(price));

    // ajax request
    const request = new XMLHttpRequest();
    request.open('POST', '/changePrice');
    request.send(data);


    // After request completes
    request.onload = () => {
        const data = JSON.parse(request.responseText);
        if (data.success){
          changeTotal(data, element);
          // console.log(data);
        }
    };

    // prevernt reload
    return false;

};


function showTotal(data) {
  // console.log(data);
/*
  Data Example:
    {data{
      item_id: 6
      quantity: "4"
      subtotal: 33
      total:
        subtotal__sum: 85
        __proto__: Object
        __proto__: Object
      }
    success: true
    __proto__: Object}
*/
  total = data.data.total.subtotal__sum
  document.querySelector("#total").innerHTML = total;
};


function calc_subtotal(element, price, item_id){

  var item_count = element.value;
  var subtotal = item_count*price;

  // console.log(id.parentElement.nextElementSibling.innerHTML);
  element.parentElement.nextElementSibling.innerHTML = subtotal;
  toEdit = [];
  var item = {
    "id" : item_id,
    "item_count" : item_count,
    "subtotal" : subtotal
  };
  toEdit.push(item);

  const data = new FormData();
  data.append('csrfmiddlewaretoken', csrftoken);
  data.append('items', JSON.stringify(toEdit));


  // ajax request
  const request = new XMLHttpRequest();
  request.open('POST', '/calc_total');
  request.send(data);


  // After request completes
  request.onload = () => {
      const data = JSON.parse(request.responseText);
      if (data.success)
          showTotal(data);
  };

  // prevernt reload
  return false;
  // alert(item_count+" "+subtotal);
};

function checkout() {

  // ajax request
  const request = new XMLHttpRequest();
  request.open('POST', '/checkout');
  request.send();

  // After request completes
  request.onload = () => {
      const data = JSON.parse(request.responseText);
      if (data.success)
          // showTotal(data);
          alert("Done");
  };

  // prevernt reload
  return false;
  // alert(item_count+" "+subtotal);
};

// Get csrf token
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
