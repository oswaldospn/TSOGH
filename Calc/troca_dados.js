function salvarDados() {

	localStorage.setItem("texto1", document.getElementById("entrada").value);
}

function recuperarDados() {

	document.getElementById("saida").value = localStorage.getItem("texto1");
}

