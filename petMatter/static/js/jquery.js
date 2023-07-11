$(function(){
    $("#form-login").validate({ 
        rules:{
            txtUsuario:{
                required: true,
                minlength:25
            },
            txtContrasena:{
                required: true,
            }
        },
        messages:{
            txtUsuario:{
                required: "Debe ingresar un rut",
            },
            txtContrasena:{
                required: "Ingrese su contraseña"
            }
        }
    })
})