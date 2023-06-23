let imgInp = document.getElementById('imagenProductoAgregar');
let blah = document.getElementById('imagenProductoAgregarMostrar');
let imgEdi = document.getElementById('imagenProductoEditar');
let blaEdi = document.getElementById('imagenProductoEditarMostrar');

console.log("js",imgEdi);


imgInp.onchange = evt => {
    const [file] = imgInp.files
    if (file) {
      blah.src = URL.createObjectURL(file)
    }
  }

  imgEdi.onchange = evt => {
    const [file] = imgEdi.files
    if (file) {
        blaEdi.src = URL.createObjectURL(file)
    }
  }