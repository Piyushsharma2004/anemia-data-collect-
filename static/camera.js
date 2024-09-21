(function() {
    var streaming = false;

    var video = null;
    var canvas = null;
    var stream = null;
    var photo = null;
    var startbutton = null;
    
    const width = 1280;
    const height = 720;
    function startup() {
        video = document.getElementById('video');
        canvas = document.getElementById('canvas');
        eye = document.getElementById('eye');
        var buttons = document.querySelectorAll('.photo_button');
        // console.log(buttons[0]);
        // console.log("HI");
        var constraints = {
            video: {
                aspectRatio: { ideal: 16/9 },
                width: { ideal: 1280 }, // You can adjust the width and height based on your preferences
            },
            audio: false,
        };
        
        function clearphoto(button) {
            var context = canvas.getContext('2d');
            context.fillStyle = "#AAA";
            context.fillRect(0, 0, canvas.width, canvas.height);
            var photo = document.getElementById(button.id.split("_")[0]);
            var data = canvas.toDataURL('image/png');
            photo.setAttribute('src', data);
          }
        
        navigator.mediaDevices.getUserMedia(constraints)
            .then(function(userStream) {
                document.getElementById("video-container").style.paddingTop = "0px";
                stream = userStream;
                video.srcObject = stream;
                video.play();
            })
            .catch(function (err) {
                console.log("An error occurred: " + err);
            });

        video.addEventListener('canplay', function (ev) {
            if (!streaming) {
                video.setAttribute('width', "100%");
                video.setAttribute('height', "100%");
                canvas.setAttribute('width', width);
                canvas.setAttribute('height', height);
                streaming = true;
            }
        }, false);

        function takepicture(button) {
            var context = canvas.getContext('2d');
            if (width && height) {
              canvas.width = width;
              canvas.height = height;
              context.drawImage(video, 0, 0, width, height);
              var data = canvas.toDataURL('image/png');
            //   console.log(button.id.split("_")[0]);
              var photo = document.getElementById(button.id.split("_")[0]);
              console.log(data);
              photo.setAttribute('src', data);
            //   console.log(photo.id+"_hidden"); 
              document.getElementById(photo.id + "_hidden").value = data;
            } else {
              clearphoto(button);
            }
          }
        buttons.forEach((button)=>{
            console.log(button);
            button.addEventListener('click', function(ev) {
                var button =ev.target;
                // Your custom functionality for generic buttons here
                takepicture(button);
                ev.preventDefault();
            }, false);
        });
        // startbutton.addEventListener('click', function(ev,){
        //     takepicture();
        //     ev.preventDefault();
        //   }, false);
    }


    window.addEventListener('load', startup, false);
})();
