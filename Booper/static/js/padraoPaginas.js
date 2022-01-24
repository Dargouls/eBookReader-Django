const logoSite = document.querySelector("#img-logo");
var dropdownAtivo = false;
var header = document.querySelector("header");

window.addEventListener("scroll", function () {
	if (window.scrollY > 100) {
		header.style = "transform: translateY(-120px);";
	} else {
		header.style = "transform: translateY(0);";
	}
});

//Funções
function dropbtn() {
	var content = document.querySelector(".dropdownContent");
	var dropdown = document.querySelector("#dropdown-mobile");
	if (dropdownAtivo) {
		dropdownAtivo = false;
		dropdown.style.width = "50px";
		content.style.display = "none";
		logoSite.style.display = "block";
		logoSite.style.opacity = "1";
	} else {
		dropdownAtivo = true;
		dropdown.style.width = "100%";
		content.style.display = "block";
		logoSite.style.opacity = "0";
		setTimeout(logoDisplay, 170);
	}
}
function logoDisplay() {
	logoSite.style.display = "none";
}
