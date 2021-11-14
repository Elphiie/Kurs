const btn = document.getElementById('btn');

btn.addEventListener("click", () => {
    if (btn.innerText === "Klikk meg!") {
        btn.innerText = "Hei, du laget en alert knapp!";
    } else {
        btn.innerText = "Klikk meg!";
    }

});
