document.body.onload = testar;
const nome = document.getElementById("nome");
console.log(nome.value);

document.getElementsByClassName("acao")[0].addEventListener("click", ()=>console.log("Flamengo"));

// document.getElementById("nome").addEventListener("change", (name)=>{
//     const nome = document.getElementById("nome");
//     console.log(nome.value);
// });

nome.addEventListener("input", ()=>{
    
    nome.style.textTransform = "capitalize";
    nome.value = nome.value.toLowerCase();
    console.log(`${nome.value}, here`)
});

function testar(){
    const elemento = document.createElement("div");
    const paragrafo = document.createElement("p");
    paragrafo.innerHTML = "oi";
    elemento.appendChild(paragrafo);
    document.body.appendChild(elemento);
}

function acao() {
    console.log("oi");
}

document.getElementsByClassName("teste")[0].onclick = ()=>{
    document.getElementById("nome").innerHTML = "<div></div>";
    document.getElementsByTagName("label")[0].innerHTML = "oi";
    document.createElement("p").innerHTML = "oi";
};


