// Модальное окно МТС

	// открыть по кнопке
	$('.js-button-campaign-mts').click(function() { 
		
		$('.js-overlay-campaign-mts').fadeIn();

	});

	// закрыть на крестик
	$('.js-close-campaign-mts').click(function() { 
		$('.js-overlay-campaign-mts').fadeOut();
		
	});

	// закрыть по клику вне окна
	$(document).mouseup(function (e) { 
		var popup = $('.js-popup-campaign-mts');
		if (e.target!=popup[0]&&popup.has(e.target).length === 0){
			$('.js-overlay-campaign-mts').fadeOut();
			
		}
	});

// Модальное окно ЦРР

	// открыть по кнопке
	$('.js-button-campaign-crd').click(function() { 
		
		$('.js-overlay-campaign-crd').fadeIn();

	});

	// закрыть на крестик
	$('.js-close-campaign-crd').click(function() { 
		$('.js-overlay-campaign-crd').fadeOut();
		
	});

	// закрыть по клику вне окна
	$(document).mouseup(function (e) { 
		var popup = $('.js-popup-campaign-crd');
		if (e.target!=popup[0]&&popup.has(e.target).length === 0){
			$('.js-overlay-campaign-crd').fadeOut();
			
		}
	});

// Модальное окно WIFI

	// открыть по кнопке
	$('.js-button-campaign-wifi').click(function() { 
		
		$('.js-overlay-campaign-wifi').fadeIn();

	});

	// закрыть на крестик
	$('.js-close-campaign-wifi').click(function() { 
		$('.js-overlay-campaign-wifi').fadeOut();
		
	});

	// закрыть по клику вне окна
	$(document).mouseup(function (e) { 
		var popup = $('.js-popup-campaign-wifi');
		if (e.target!=popup[0]&&popup.has(e.target).length === 0){
			$('.js-overlay-campaign-wifi').fadeOut();
			
		}
	});

// Модальное окно nav

	// открыть по кнопке
	$('.js-button-campaign-nav').click(function() { 
		
		$('.js-overlay-campaign-nav').fadeIn();

	});

	// закрыть на крестик
	$('.js-close-campaign-nav').click(function() { 
		$('.js-overlay-campaign-nav').fadeOut();
		
	});

	// закрыть по клику вне окна
	$(document).mouseup(function (e) { 
		var popup = $('.js-popup-campaign-nav');
		if (e.target!=popup[0]&&popup.has(e.target).length === 0){
			$('.js-overlay-campaign-nav').fadeOut();
			
		}
	});

// Модальное окно faq

	// открыть по кнопке
	$('.js-button-campaign-faq').click(function() { 
		
		$('.js-overlay-campaign-faq').fadeIn();
		
	});

	// закрыть на крестик
	$('.js-close-campaign-faq').click(function() { 
		$('.js-overlay-campaign-faq').fadeOut();
		
	});

	// закрыть по клику вне окна
	$(document).mouseup(function (e) { 
		var popup = $('.js-popup-campaign-faq');
		if (e.target!=popup[0]&&popup.has(e.target).length === 0){
			$('.js-overlay-campaign-faq').fadeOut();
			
		}
	});

// Модальное окно lang

	// открыть по кнопке
	$('.js-button-campaign-lang').click(function() { 
		
		$('.js-overlay-campaign-lang').fadeIn();

	});

	// закрыть на крестик
	$('.js-close-campaign-lang').click(function() { 
		$('.js-overlay-campaign-lang').fadeOut();
		
	});

	// закрыть по клику вне окна
	$(document).mouseup(function (e) { 
		var popup = $('.js-popup-campaign-lang');
		if (e.target!=popup[0]&&popup.has(e.target).length === 0){
			$('.js-overlay-campaign-lang').fadeOut();
			
		}
	});

	function ru(){
		window.location.replace('http://127.0.0.1:5000/ru');
	}

	function en(){
		window.location.replace('http://127.0.0.1:5000/en');	
	}

	function ch(){
		window.location.replace('http://127.0.0.1:5000/ch');
	}



// Модальное окно about
	var video;
	var myaudio = new Audio('about.mp3');

	window.onload = function(){
		video = document.getElementById("video");
		myaudio = document.getElementById("myaudio");
	}

	// открыть по кнопке
	$('.js-button-campaign-about').click(function() { 
		
		$('.js-overlay-campaign-about').fadeIn();

	});

	// закрыть на крестик
	$('.js-close-campaign-about').click(function() { 
		$('.js-overlay-campaign-about').fadeOut();
		
	});

	// закрыть по клику вне окна
	$(document).mouseup(function (e) { 
		var popup = $('.js-popup-campaign-about');
		if (e.target!=popup[0]&&popup.has(e.target).length === 0){
			$('.js-overlay-campaign-about').fadeOut();
			video.currentTime  = 0;
			video.pause();
			myaudio.currentTime  = 0;
			myaudio.pause();
			
		}
	});
