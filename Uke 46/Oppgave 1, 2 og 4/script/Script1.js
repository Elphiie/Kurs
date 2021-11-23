'use strict';



var pattern = ['ArrowUp', 'ArrowUp', 'ArrowDown', 'ArrowDown', 'ArrowLeft', 'ArrowRight', 'ArrowLeft', 'ArrowRight', 'b', 'a'];
var current = 0;
var cheat = document.getElementById("code");
const btn = document.getElementById("btn");
var ans = document.getElementById("ans");


var keyHandler = function (event) {

	if (pattern.indexOf(event.key) < 0 || event.key !== pattern[current]) {
		current = 0;
		return;
	}

	current++;

	if (pattern.length === current) {
		current = 0;
		cheat.innerHTML = 'POG';
	}

};

document.addEventListener('keydown', keyHandler, false);

btn.addEventListener("click", no)
function no() {
	ans.innerHTML = 'Git gud';
}
