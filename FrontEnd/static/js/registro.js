function send_form() {

    var url = "http://localhost:5000/api/tiendas"

    var input_nombre = document.querySelector('#nombre').value;
    var input_direccion = document.querySelector('#inputAddress').value;
    var input_cel = document.querySelector('#inputtelefono').value;
    var input_categoria = document.querySelector('#inputcategoria').value;
    var input_img = document.querySelector('#cargaimg').value; 

	var r = new XMLHttpRequest();
    r.open('POST', url);


    /*var form = {
        "nombre_tienda": input_nombre,
        "direccion_tienda": input_direccion,
        "categoria": input_categoria,
        "imagen_portada_tienda": input_img,
        "contacto": input_cel
    };*/

    var form = new FormData(formElem);
    console.log(form.entries);

	r.send( form );
    
	r.onload = function load() {
        json = r.response;
        window.location.replace("http://localhost/tiendas/" + json.id_tienda);
    }
    return false;
}