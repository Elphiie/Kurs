const btn = document.getElementById("btn");

btn.addEventListener("click", ()=>{

    if(btn.innerText === "Les mer"){
        btn.innerText = "Denied!";
    }else{
      btn.innerText= "Les mer";
    }
});
