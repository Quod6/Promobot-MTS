var video;
var myaudio = new Audio('about.mp3');

window.onload = function(){
	video = document.getElementById("video");
	myaudio = document.getElementById("myaudio");
}

function about(){
	video.play();
	myaudio.play();
}

function PlayPause(){
	if(video.paused){
		video.play();
		myaudio.play();
	}
	else{
		video.pause();
		myaudio.pause();
	}
}

function StopPlay(){
	video.currentTime  = 0;
	video.play();
	myaudio.currentTime  = 0;
	myaudio.play();
}

function StopPause(){
	video.currentTime  = 0;
	video.pause();
	myaudio.currentTime  = 0;
	myaudio.pause();
}
