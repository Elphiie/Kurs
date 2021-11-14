const ttl = document.getElementById('ttl');

const txt = document.getElementById('txt');

const btn = document.getElementById('btn');

btn.addEventListener("click", () => {

    if (ttl.innerText === "Overskrift") {
        ttl.innerText = "Ny overskrift";

    } else {
        ttl.innerText = "Overskrift";

    }

    if (txt.innerText === "Tekst") {
        txt.innerText = "Annen tekst";

    } else {
        txt.innerText = "Tekst";

    }

});
