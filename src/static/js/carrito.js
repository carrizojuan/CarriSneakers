var btnsAgregarCarrito = document.getElementsByClassName('agregar-carrito');
for (var i = 0; i < btnsAgregarCarrito.length; i++) {
    btnsAgregarCarrito[i].addEventListener('click', function() {
        var producto_id = this.dataset.producto
        var action = this.dataset.action
        
        if (user === "AnonymousUser") {
            console.log("No permission")
        }else{
            updateOrdenUsuario(producto_id, action)
        }
    });
}

function updateOrdenUsuario(producto_id, action) {
    var url = "/update_item/"

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({ 'producto_id': producto_id, 'action': action})
    })
    .then(response => 
        response.json()
    )
    .then(data => {
        console.log('data:', data);
    })
}