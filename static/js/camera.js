document.addEventListener('DOMContentLoaded', function () {

    // References to all the element we will need.
    var video = document.querySelector('#camera-stream'),
        image = document.querySelector('#snap'),
        start_camera = document.querySelector('#start-camera'),
        controls = document.querySelector('.controls'),
        take_photo_btn = document.querySelector('#take-photo'),
        delete_photo_btn = document.querySelector('#delete-photo'),
        download_photo_btn = document.querySelector('#download-photo'),
        error_message = document.querySelector('#error-message');
        overlay = document.querySelector('#overlay');
        terminator = document.querySelector('#overlay-t');
        matrix = document.querySelector('#overlay-m');
        status = 0;


    // The getUserMedia interface is used for handling camera input.
    // Some browsers need a prefix so here we're covering all the options
    navigator.getMedia = ( navigator.getUserMedia ||
    navigator.webkitGetUserMedia ||
    navigator.mozGetUserMedia ||
    navigator.msGetUserMedia);


    if(!navigator.getMedia){
        displayErrorMessage("Your browser doesn't have support this function.");
    }
    else{

        // Request the camera.
        navigator.getMedia(
            {
                video: true
            },
            // Success Callback
            function(stream){

                // Create an object URL for the video stream and
                // set it as src of our HTLM video element.
                video.src = window.URL.createObjectURL(stream);

                // Play the video element to start the stream.
                video.play();
                video.onplay = function() {
                    showVideo();
                };
         
            },
            // Error Callback
            function(err){
                displayErrorMessage("There was an error with accessing the camera stream: " + err.name, err);
            }
        );

    }



    // Mobile browsers cannot play video without user input,
    // so here we're using a button to start it manually.
    start_camera.addEventListener("click", function(e){

        e.preventDefault();

        // Start video playback manually.
        video.play();
        showVideo();

    });


    take_photo_btn.addEventListener("click", function(e){

        e.preventDefault();

        var snap = takeSnapshot();

        $(' #camera-stream ').css('-webkit-filter', 'grayscale(100%)');
                $(' #camera-stream ').css('filter', 'grayscale(100%)');

        // Show image. 
        image.setAttribute('src', snap);
        image.classList.add("visible");

        // Enable delete and save buttons
        delete_photo_btn.classList.remove("disabled");
        download_photo_btn.classList.remove("disabled");
        $(' #overlay ').css('opacity', '0.5');


        // Set the href attribute of the download button to the snap url.
        download_photo_btn.href = snap;

        // Pause video playback of stream.
        video.pause();

    });


    delete_photo_btn.addEventListener("click", function(e){

        e.preventDefault();

        // Hide image.
        image.setAttribute('src', "");
        image.classList.remove("visible");

        // Disable delete and save buttons
        delete_photo_btn.classList.add("disabled");
        download_photo_btn.classList.add("disabled");
        $(' #overlay ').css('opacity', '0');

        // Resume playback of stream.
        video.play();

    });


  
    function showVideo(){
        // Display the video stream and the controls.

        hideUI();
        video.classList.add("visible");
        controls.classList.add("visible");
    }

    function gray(r, g, b) {
        var avg = 0.3 * r + 0.59 * g + 0.11 * b;
        return [avg, avg, avg, 255];
    }

    function takeSnapshot(){
        // Here we're using a trick that involves a hidden canvas element.  

        var hidden_canvas = document.querySelector('canvas'),
            context = hidden_canvas.getContext('2d');

        var width = video.videoWidth,
            height = video.videoHeight;

        if (width && height) {

            // Setup a canvas with the same dimensions as the video.
            hidden_canvas.width = width;
            hidden_canvas.height = height;

            // Make a copy of the current frame in the video on the canvas.
            if (status == 0) {
                $(' #camera-stream ').css('-webkit-filter', 'none');
                $(' #camera-stream ').css('filter', 'none');
                context.drawImage(video, 0, 0, width, height);
            }
            if (status == 1) {
                $(' #camera-stream ').css('-webkit-filter', 'none');
                $(' #camera-stream ').css('filter', 'none');
                context.drawImage(video, 0, 0, width, height);
                context.drawImage(terminator, 0, 0, width, height);
            }
            if (status == 2) {
                $(' #camera-stream ').css('-webkit-filter', 'grayscale(100%)');
                $(' #camera-stream ').css('filter', 'grayscale(100%)');
                context.drawImage(video, 0, 0, width, height);
                context.drawImage(matrix, 0, 0, width, height);
            }
            
            
            // Turn the canvas image into a dataURL that can be used as a src for our photo.
            return hidden_canvas.toDataURL('image/png');


        }
    }


    function displayErrorMessage(error_msg, error){
        error = error || "";
        if(error){
            console.error(error);
        }

        error_message.innerText = error_msg;

        hideUI();
        error_message.classList.add("visible");
    }

   
    function hideUI(){
        // Helper function for clearing the app UI.

        controls.classList.remove("visible");
        start_camera.classList.remove("visible");
        video.classList.remove("visible");
        snap.classList.remove("visible");
        error_message.classList.remove("visible");
        $('.js-overlay-campaign-save').fadeOut();
    }

});




//--------my-functions--------//

filter = document.querySelector('#filter_selector');

function showFilter(){
    $(' #filter_selector ').css('opacity', '1');
    $(' .app ').css('margin-top', '0px');

    // var start = Date.now(); // сохранить время начала
    //     i = 0;

    // var timer = setInterval(function() {
    //   // вычислить сколько времени прошло с начала анимации
    //   var timePassed = Date.now() - start;

    //   if (i == 275) {
    //     clearInterval(timer); // конец через 2 секунды
    //     return;
    //   }

    //   // рисует состояние анимации, соответствующее времени timePassed
    //   draw(timePassed);
    //   i = i+25;

    // }, 1);

    // // в то время как timePassed идёт от 0 до 2000
    // // left принимает значения от 0 до 400px
    // function draw(timePassed) {
    //   $(' #filter_selector ').css('margin-top', -250+i + "px");
    //   $(' .app ').css('margin-top', -250+i +  'px');
    // }
}

function hideFilter(){
    $(' #filter_selector ').css('opacity', '0');
    $(' .app ').css('margin-top', '-250px');
    // $(' #filter_selector ').css('margin-top', '0px');
    // $(' .app ').css('margin-top', '0px');
    // var start = Date.now(); // сохранить время начала
    //     i = 0;

    // var timer = setInterval(function() {
    //   // вычислить сколько времени прошло с начала анимации
    //   var timePassed = Date.now() - start;

    //   if (i == 275) {
    //     clearInterval(timer); // конец через 2 секунды
    //     return;
    //   }

    //   // рисует состояние анимации, соответствующее времени timePassed
    //   draw(timePassed);
    //   i = i+25;

    // }, 1);

    // // в то время как timePassed идёт от 0 до 2000
    // // left принимает значения от 0 до 400px
    // function draw(timePassed) {
    //   $(' #filter_selector ').css('margin-top', 0-i + "px");
    //   $(' .app ').css('margin-top', 0-i +  'px');
    // }
}


function Terminator(){
    $(' #overlay-t ').css('opacity', '0.7');
    $(' #camera-stream ').css('opacity', '1');
    $(' #overlay-m ').css('opacity', '0');
    $(' #camera-stream ').css('-webkit-filter', 'none');
    $(' #camera-stream ').css('filter', 'none');
    status = 1;
}
function Matrix(){
    $(' #camera-stream ').css('opacity', '0.5');
    $(' #overlay-t ').css('opacity', '0');
    $(' #overlay-m ').css('opacity', '0.9');
    $(' #camera-stream ').css('-webkit-filter', 'grayscale(100%)');
    $(' #camera-stream ').css('filter', 'grayscale(100%)');
    status = 2;
}

function Fclear(){
    $(' #overlay-t ').css('opacity', '0');
    $(' #camera-stream ').css('opacity', '1');
    $(' #overlay-m ').css('opacity', '0');
    $(' #camera-stream ').css('-webkit-filter', 'none');
    $(' #camera-stream ').css('filter', 'none');
    status = 0;
}

function preSendMail(){
    setTimeout(function(){ 
        window.location.replace('http://127.0.0.1:5000/email-send');
    }, 1000);
}

function SendMail(){
    setTimeout(function(){ 
        window.location.replace('http://127.0.0.1:5000/send-mail/');
        }, 1000);
}