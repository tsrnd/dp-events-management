(function($) {
	"use strict";

	$(document).ready(function(){

		$('.widget.widget_tag_cloud .tagcloud a, .widget.widget_product_tag_cloud .tagcloud a').removeAttr('style');

  		$( "#header-menu" ).clone().appendTo( ".sb-slidebar.sb-left, .sb-slidebar.sb-right" ).removeClass('header-menu sf-menu').addClass('menu-slidebar');

		if(jQuery.isFunction($().superfish)) {
			$('ul.sf-menu').superfish({
				speed: 1,
				speedOut: 1
			});
  		}

		if(jQuery.isFunction($.slidebars)) {
			$.slidebars();
  		}

		if(jQuery.isFunction($().owlCarousel)) {
			$(".ltr .home-slider-events-active").owlCarousel({
				loop:true,
			    nav:true,
			    navText:['<span class="slide-prev-nav"><i class="fa fa-angle-left"></i></span>','<span class="slide-next-nav"><i class="fa fa-angle-right"></i></span>'],
			    dots:false,
			    items:1,
			    smartSpeed: 1000,
			    autoplay: true,
				autoplayHoverPause: true,
			    animateOut: 'fadeOut'
			});
			$(".ltr .home-testimonials .testimonial-loop").owlCarousel({
				loop:true,
			    nav:true,
			    navText:['<span class="testi-prev-nav"><i class="fa fa-angle-left"></i></span>','<span class="testi-next-nav"><i class="fa fa-angle-right"></i></span>'],
			    responsiveClass:true,
			    items:1,
			    smartSpeed: 2000,
			    autoplayTimeout: 8000,
			    autoplay: true,
				autoplayHoverPause: true
			});
			$(".ltr div.images .thumbnails").owlCarousel({
				loop:true,
			    nav:true,
			    navText:['<span class="owl-prev-nav"><i class="fa fa-angle-left"></i></span>','<span class="owl-next-nav"><i class="fa fa-angle-right"></i></span>'],
			    margin:10,
			    responsiveClass:true,
			    responsive:{
			        0:{
			            items:3,
			            nav:true
			        },
			        768:{
			            items:5,
			            nav:true,
			            loop:true
			        },
			        992:{
			            items:7,
			            nav:true,
			            loop:true
			        }
			    }
			});

			$(".rtl .home-slider-events-active").owlCarousel({
				rtl:true,
				loop:true,
			    nav:true,
			    navText:['<span class="slide-prev-nav"><i class="fa fa-angle-left"></i></span>','<span class="slide-next-nav"><i class="fa fa-angle-right"></i></span>'],
			    dots:false,
			    items:1,
			    smartSpeed: 1000,
			    autoplay: true,
				autoplayHoverPause: true,
			    animateOut: 'fadeOut'
			});
			$(".rtl .home-testimonials .testimonial-loop").owlCarousel({
				rtl:true,
				loop:true,
			    nav:true,
			    navText:['<span class="testi-prev-nav"><i class="fa fa-angle-left"></i></span>','<span class="testi-next-nav"><i class="fa fa-angle-right"></i></span>'],
			    responsiveClass:true,
			    items:1,
			    smartSpeed: 2000,
			    autoplayTimeout: 8000,
			    autoplay: true,
				autoplayHoverPause: true
			});
			$(".rtl div.images .thumbnails").owlCarousel({
				rtl:true,
				loop:true,
			    nav:true,
			    navText:['<span class="owl-prev-nav"><i class="fa fa-angle-left"></i></span>','<span class="owl-next-nav"><i class="fa fa-angle-right"></i></span>'],
			    margin:10,
			    responsiveClass:true,
			    responsive:{
			        0:{
			            items:3,
			            nav:true
			        },
			        768:{
			            items:5,
			            nav:true,
			            loop:true
			        },
			        992:{
			            items:7,
			            nav:true,
			            loop:true
			        }
			    }
			});

		}

		if(jQuery.isFunction($().magnificPopup)) {
			$('.gallery-image a').magnificPopup({
				type: 'image',
				gallery:{
					enabled:true
				}
			});
		}

        $("#back-top").hide();
        $(window).scroll(function () {
            if ($(this).scrollTop() > 300) {
                $('#back-top').fadeIn();
            } else {
                $('#back-top').fadeOut();
            }
        });
        $('#back-top').click(function () {
            $('body,html').animate({scrollTop: 0}, 800);
            return false;
        });

		if ( $('.tribe-events-tickets').length ) {
			$('.tribe-events-tickets').parent('.cart').attr('id', 'tribe-events-tickets');
			$('.tribe-events-cta-btn a').attr('href', '#tribe-events-tickets');
		}
		if ( $('.eventbrite-ticket-embed').length ) {
			$('.eventbrite-ticket-embed').attr('id', 'eventbrite-ticket-embed');
			$('.tribe-events-cta-btn a').attr('href', '#eventbrite-ticket-embed');
		}
		if ( $('.tribe-events-pagination .next').length && !$('.tribe-events-pagination .next a').length ) {
			$('.tribe-events-pagination .next').hide();
		}
		if ( $('.tribe-events-pagination .prev').length && !$('.tribe-events-pagination .prev a').length ) {
			$('.tribe-events-pagination .prev').hide();
		}
		if ( $('.tribe-events-pagination').length && !$('.tribe-events-pagination .next a').length && !$('.tribe-events-pagination .prev a').length ) {
			$('.tribe-events-pagination').hide();
		}

	});

	jQuery(document).on("scroll",function(){
		if( jQuery(document).scrollTop() > 140) {
			jQuery("body.sticky-header-yes").removeClass("header-large").addClass("header-small");
		}
		else {
			jQuery("body.sticky-header-yes").removeClass("header-small").addClass("header-large");
		}
	});

})(jQuery);