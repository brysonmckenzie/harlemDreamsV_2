// 2. This code loads the IFrame Player API code asynchronously.
var tag = document.createElement('script');

tag.src = "https://www.youtube.com/iframe_api";
var firstScriptTag = document.getElementsByTagName('script')[0];
firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);

// 3. This function creates an <iframe> (and YouTube player)
//    after the API code downloads.
var player;
function onYouTubeIframeAPIReady() {
    player = new YT.Player('player', {
        height: '390',
        width: '640',
        // videoId: 'J7wx-U_3AeI',
        videoId: 'Hua4MRTKmy0',
        playerVars: { 'autoplay': 1, 'controls': 0, 'rel': 0, 'modestbranding': true },
        events: {
            'onReady': onPlayerReady,

        }
    });
}

// 4. The API will call this function when the video player is ready.
function onPlayerReady(event) {
    // player.setPlaybackRate(1);
    // event.target.playVideo();
    // player.mute();


    // Update the controls on load
    updateTimerDisplay();
    updateProgressBar();

    // Clear any old interval.
    clearInterval(time_update_interval);

    // Start interval to update elapsed time display and
    // the elapsed part of the progress bar every second.
    time_update_interval = setInterval(function () {
        updateTimerDisplay();
        updateProgressBar();
    }, 1000)




    // This function is called by initialize()
    function updateTimerDisplay() {
        // Update current time text display.
        $('#current-time').text(formatTime(player.getCurrentTime()));
        $('#duration').text(formatTime(player.getDuration()));
    }

    function formatTime(time) {
        time = Math.round(time);

        var minutes = Math.floor(time / 60),
            seconds = time - minutes * 60;

        seconds = seconds < 10 ? '0' + seconds : seconds;

        return minutes + ":" + seconds;
    }



}


// 5. The API calls this function when the player's state changes.
//    The function indicates that when playing a video (state=1),
//    the player should play for six seconds and then stop.
var done = false;
function onPlayerStateChange(event) {
    if (event.data == YT.PlayerState.PLAYING && !done) {
        setTimeout(stopVideo, 6000);
        done = true;
    }



}


function stopVideo() {
    player.stopVideo();
}

// function mute() {
//     document.getElementById("mute-toggle").toggleClass('fas fa-volume-mute');

//     player.mute();
//  }


var muteBtn = document.getElementById("muteButton")
var muteIcon = document.getElementById("speaker")
var muteContains = muteIcon.classList.contains("fa-volume-up")
var muteContainsList = muteIcon.classList

muteBtn.addEventListener('click', function (event) {
    console.log(player);
    console.log(muteContains);
    console.log(muteContainsList);

    console.log('speaker')

    if (!!player.isMuted()) {
        player.unMute();
        



    } else {
        player.mute();
        muteIcon.style.color = "#FF0000"


    }



});


