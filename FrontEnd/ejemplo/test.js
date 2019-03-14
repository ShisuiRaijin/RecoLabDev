document.addEventListener("DOMContentLoaded", function(){

	/* Request for the json */
	var url = "http://127.0.0.1:5000/api/tiendas";
	var r = new XMLHttpRequest();
    r.open('GET', url);
    r.responseType = '';
	r.send();
	
	r.onload = function loadGames() {
        var json = r.response;
		var elem = document.getElementById("out");
        
        elem.innerText = json

	}
})