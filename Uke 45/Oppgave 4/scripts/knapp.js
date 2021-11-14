'use strict';

const btn = document.getElementById('btn');

const dl = document.getElementById('dl');

var count = 1;

btn.addEventListener("click", () => {
    dl.innerText = count;
    count++
});
