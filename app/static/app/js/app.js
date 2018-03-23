'use strict';

function VideoPlayer() {

    this.video = document.createElement('video');
    this.video.src = video_url;
    this.video.controls = true;

    this.videoPlayerWrapper = $('#videoPlayerWrapper');
}

VideoPlayer.prototype.play = function() {
    var video = this.video;
    if (video.paused) {
        video.play();
    }
};
VideoPlayer.prototype.pause = function() {
    var video = this.video;
    video.pause();
};

VideoPlayer.prototype.setVideoPlayerWrapperSize = function(width, height) {
    var videoPlayerWrapper = this.videoPlayerWrapper;
    videoPlayerWrapper.width(width);
    videoPlayerWrapper.height(height);
};

VideoPlayer.prototype.init = function() {
    var self = this;
    var video = self.video;

    $(videoPlayerWrapper).prepend(video);
    this.setVideoPlayerWrapperSize(video.videoWidth, video.videoHeight);
    this.play();
    CHARLIE.setup(video);

};
VideoPlayer.prototype.setControlState = function() {};

$(document).ready(function() {
    var vPlayer = new VideoPlayer();
    var video = vPlayer.video;
    video.addEventListener('loadedmetadata', function() {
        vPlayer.init();
    });
});
