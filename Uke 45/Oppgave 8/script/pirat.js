'use strict';

var x = document.getElementById('myAudio');

function playAudio() {
    x.play();
}

function pauseAudio() {
    x.pause();
}


function download(filename, text) {
var element = document.createElement('a');
element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
element.setAttribute('download', "../media/fools.mp3");

    element.style.display = 'none';
    document.body.appendChild(element);

    element.click();

    document.body.removeChild(element);

}