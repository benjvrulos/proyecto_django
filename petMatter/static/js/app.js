"use strict";
//Variable que mantiene el estado visible del carrito
var carritoVisible = false;
// eliminarStorageCarrito();
crearStorageCarrito();
cargarStorageCarrito();
//Espermos que todos los elementos de la pàgina cargen para ejecutar el script
if (document.readyState == "loading") {
  document.addEventListener("DOMContentLoaded", ready);
} else {
  ready();
}

function ready() {
  //funcionalidad a los botones de eliminar del carro
  var botonesEliminarItem = document.getElementsByClassName("btn-eliminar");
  for (var i = 0; i < botonesEliminarItem.length; i++) {
    var button = botonesEliminarItem[i];
    button.addEventListener("click", eliminarItemCarrito);
  }

  //funcionalidad al boton de sumar cantidad
  var botonesSumarCantidad = document.getElementsByClassName("sumar-cantidad");
  for (var i = 0; i < botonesSumarCantidad.length; i++) {
    var button = botonesSumarCantidad[i];
    button.addEventListener("click", sumarCantidad);
  }

  //funcionalidad al buton de restar cantidad
  var botonesRestarCantidad =
    document.getElementsByClassName("restar-cantidad");
  for (var i = 0; i < botonesRestarCantidad.length; i++) {
    var button = botonesRestarCantidad[i];
    button.addEventListener("click", restarCantidad);
  }

  //funcionalidad al boton de agregar al carrito
  var botonesAgregarAlCarrito = document.getElementsByClassName("boton-item");
  for (var i = 0; i < botonesAgregarAlCarrito.length; i++) {
    var button = botonesAgregarAlCarrito[i];
    button.addEventListener("click", agregarAlCarritoClicked);
  }

  //funcionalidad al botón comprar (tira un aviso por consola)
  document
    .getElementsByClassName("btn-pagar")[0]
    .addEventListener("click", pagarClicked);
}

//se eliminan todos los elementos del carrito y se oculta automaticamente
function pagarClicked() {
  alert("Gracias por la compra");
  //Elimino todos los elmentos del carrito
  var carritoItems = document.getElementsByClassName("carrito-items")[0];
  while (carritoItems.hasChildNodes()) {
    carritoItems.removeChild(carritoItems.firstChild);
  }
  actualizarTotalCarrito();
  ocultarCarrito();
}

// Crear Storage para carrito

function eliminarStorageCarrito() {
  localStorage.removeItem("myStorage");
}
function crearStorageCarrito() {
  let array;
  let storage = JSON.parse(localStorage.getItem("myStorage"));
  if (storage) {
  } else {
    array = [];
    const obj = JSON.stringify(array);
    localStorage.setItem("myStorage", obj);
  }
}

function cargarStorageCarrito() {
  let storage = JSON.parse(localStorage.getItem("myStorage"));
  console.log(storage);
  if (storage) {
    storage.forEach((producto) => {
      agregarItemAlCarrito(
        producto.titulo,
        producto.precio,
        producto.imagenSrc,
        producto.cantidad
      );
    });

    hacerVisibleCarrito();
  }
}

//esta duncion controla el boton clickeado de agregar al carrito
function agregarAlCarritoClicked(event) {
  var button = event.target;
  var item = button.parentElement;
  var titulo = item.getElementsByClassName("titulo-item")[0].innerText;
  var precio = item.getElementsByClassName("precio-item")[0].innerText;
  var imagenSrc = item.getElementsByClassName("img-item")[0].src;
  var sku = item.getElementsByClassName("skuProductoEscondido")[0].innerText;
  agregarItemAlCarrito(titulo, precio, imagenSrc);
  let storage = JSON.parse(localStorage.getItem("myStorage"));

  let itemRepetido = storage.find((i) => i.titulo == titulo);
  if (itemRepetido) {
    let cantidadAnterior = itemRepetido.cantidad;

    let index = storage.indexOf(itemRepetido);
    storage[index] = {
      sku,
      titulo,
      precio,
      imagenSrc,
      cantidad: cantidadAnterior + 1,
    };
  } else {
    storage.push({ sku,titulo, precio, imagenSrc, cantidad: 1 });
  }

  // storage.push(precioFinal);
  localStorage.setItem("myStorage", JSON.stringify(storage));

  hacerVisibleCarrito();
}

//funcion que hace visible al carrito
function hacerVisibleCarrito() {
  carritoVisible = true;
  var carrito = document.getElementsByClassName("carrito")[0];
  carrito.style.marginRight = "0";
  carrito.style.opacity = "1";

  var items = document.getElementsByClassName("contenedor-items")[0];
  items.style.width = "60%";
}

//funcion que agrega un item al carrito
function agregarItemAlCarrito(titulo, precio, imagenSrc, cantidad = 1) {
  var item = document.createElement("div");
  item.classList.add = "item";
  var itemsCarrito = document.getElementsByClassName("carrito-items")[0];

  //controlamos que el item que intenta ingresar no se encuentre en el carrito (si el item ya esta en el carrito tira una alerta que ya se encuentra)
  var nombresItemsCarrito = itemsCarrito.getElementsByClassName(
    "carrito-item-titulo"
  );
  for (var i = 0; i < nombresItemsCarrito.length; i++) {
    if (nombresItemsCarrito[i].innerText == titulo) {
      nombresItemsCarrito[i].parentElement.querySelector("input").value++;
      let precioTotal = document.querySelector(
        ".carrito-precio-total"
      ).textContent;
      let precioItem = parseFloat(precio.replace("$", "").replace(".", ""));
      let precioTotalNumber = parseFloat(
        precioTotal.replace("$", "").replace(".", "")
      );
      document.querySelector(".carrito-precio-total").textContent = `$${(
        precioItem + precioTotalNumber
      ).toLocaleString("es")},00`;
      return;
    }
  }

  var itemCarritoContenido = `
        <div class="carrito-item">
            <img src="${imagenSrc}" width="80px" alt="">
            <div class="carrito-item-detalles">
                <span class="carrito-item-titulo">${titulo}</span>
                <div class="selector-cantidad">
                    <i class="fa-solid fa-minus restar-cantidad"></i>
                    <input type="text" value="${cantidad}" class="carrito-item-cantidad" disabled>
                    <i class="fa-solid fa-plus sumar-cantidad"></i>
                </div>
                <span class="carrito-item-precio">${precio}</span>
            </div>
            <button class="btn-eliminar">
                <i class="fa-solid fa-trash"></i>
            </button>
        </div>
    `;
  item.innerHTML = itemCarritoContenido;
  itemsCarrito.append(item);

  //se agrega funcionalidad eliminar al nuevo item
  item
    .getElementsByClassName("btn-eliminar")[0]
    .addEventListener("click", eliminarItemCarrito);

  //se agrega funcionalidad restar cantidad del nuevo item
  var botonRestarCantidad = item.getElementsByClassName("restar-cantidad")[0];
  botonRestarCantidad.addEventListener("click", restarCantidad);

  //se agrega funcionalidad sumar cantidad del nuevo item
  var botonSumarCantidad = item.getElementsByClassName("sumar-cantidad")[0];
  botonSumarCantidad.addEventListener("click", sumarCantidad);

  //actualizacion total
  actualizarTotalCarrito();
}
//Aumento en uno la cantidad del elemento seleccionado
function sumarCantidad(event) {
  const storage = JSON.parse(localStorage.getItem("myStorage"));
  var buttonClicked = event.target;
  var selector = buttonClicked.parentElement;
  
  const nombreItem = selector.parentElement.querySelector(
    ".carrito-item-titulo"
  ).textContent;
  const itemRestarCantidad = storage.find((item) => item.titulo == nombreItem);
  const index = storage.indexOf(itemRestarCantidad);
  let { sku,titulo, imagenSrc, precio, cantidad } = itemRestarCantidad;
  storage[index] = {
    sku,
    titulo,
    imagenSrc,
    precio,
    cantidad: cantidad + 1,
  };
  localStorage.setItem("myStorage", JSON.stringify(storage));
  var cantidadActual = selector.getElementsByClassName(
    "carrito-item-cantidad"
  )[0].value;
  cantidadActual++;
  selector.getElementsByClassName("carrito-item-cantidad")[0].value =
    cantidadActual;
  actualizarTotalCarrito();
}
//Resto en uno la cantidad del elemento seleccionado
function restarCantidad(event) {
  const storage = JSON.parse(localStorage.getItem("myStorage"));
  var buttonClicked = event.target;
  var selector = buttonClicked.parentElement;
  
  const nombreItem = selector.parentElement.querySelector(
    ".carrito-item-titulo"
  ).textContent;
  const itemRestarCantidad = storage.find((item) => item.titulo == nombreItem);
  const index = storage.indexOf(itemRestarCantidad);
  let { sku,titulo, imagenSrc, precio, cantidad } = itemRestarCantidad;
  storage[index] = {
    sku,
    titulo,
    imagenSrc,
    precio,
    cantidad: cantidad - 1,
  };
  localStorage.setItem("myStorage", JSON.stringify(storage));

  var cantidadActual = selector.getElementsByClassName(
    "carrito-item-cantidad"
  )[0].value;
  cantidadActual--;
  if (cantidadActual >= 1) {
    selector.getElementsByClassName("carrito-item-cantidad")[0].value =
      cantidadActual;
    actualizarTotalCarrito();
  }
}

//eliminar item del carrito
function eliminarItemCarrito(event) {
  var buttonClicked = event.target;
  buttonClicked.parentElement.parentElement.remove();
  const nombreItem = buttonClicked.parentElement.parentElement.querySelector(
    ".carrito-item-titulo"
  ).textContent;
  const storage = JSON.parse(localStorage.getItem("myStorage"));
  const carritoFiltrado = storage.filter((item) => item.titulo != nombreItem);
  localStorage.setItem("myStorage", JSON.stringify(carritoFiltrado));

  //actualizamos el total del carrito
  actualizarTotalCarrito();

  //Si no hay items se oculta el carrito
  ocultarCarrito();
}
//esta funcion controla si hay elementos en el carrito. Si no hay items oculto el carrito.
function ocultarCarrito() {
  var carritoItems = document.getElementsByClassName("carrito-items")[0];
  if (carritoItems.childElementCount == 0) {
    var carrito = document.getElementsByClassName("carrito")[0];
    carrito.style.marginRight = "-100%";
    carrito.style.opacity = "0";
    carritoVisible = false;

    var items = document.getElementsByClassName("contenedor-items")[0];
    items.style.width = "100%";
  }
}
//Actualizamos el total de Carrito
function actualizarTotalCarrito() {
  //seleccionamos el contenedor carrito
  var carritoContenedor = document.getElementsByClassName("carrito")[0];
  var carritoItems = carritoContenedor.getElementsByClassName("carrito-item");
  var total = 0;
  //recorremos cada elemento del carrito para actualizar el total
  for (var i = 0; i < carritoItems.length; i++) {
    var item = carritoItems[i];
    var precioElemento = item.getElementsByClassName("carrito-item-precio")[0];
    //quitamos el simobolo peso y el punto de milesimos.
    var precio = parseFloat(
      precioElemento.innerText.replace("$", "").replace(".", "")
    );
    var cantidadItem = item.getElementsByClassName("carrito-item-cantidad")[0];
    var cantidad = cantidadItem.value;
    total = total + precio * cantidad;
  }
  total = Math.round(total * 100) / 100;

  document.getElementsByClassName("carrito-precio-total")[0].innerText =
    "$" + total.toLocaleString("es") + ",00";
}
