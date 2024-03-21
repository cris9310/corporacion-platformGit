


$(document).ready(function () {
  window.onload = codeAddress;
});

function codeAddress() {
  var URLactual = (window.location.pathname).toString().split("/")[2];
  const urlParams = new URLSearchParams(window.location.search);

  let contenido = document.querySelectorAll(".menu-links li a"),
    contenidoTotal = document.querySelectorAll(".menu-links li")
  for (let x in contenido) {
    var variableDinamica = (contenido[x].getAttribute("href")).toString().split("/")[2];
    if (URLactual == variableDinamica) {
      $(".is-active").removeClass("is-active");
      contenidoTotal[x].className += "is-active"
      break;

    }
  }

  if (urlParams == "order=todos") {
    $("#todos").prop("checked", true);
    $("#activos").prop("checked", false);
    $("#inactivos").prop("checked", false);
  } else if (urlParams == "order=activos") {
    $("#activos").prop("checked", true);
    $("#todos").prop("checked", false);
    $("#inactivos").prop("checked", false);
  } else if (urlParams == "order=inactivos") {
    $("#inactivos").prop("checked", true);
    $("#todos").prop("checked", false);
    $("#activos").prop("checked", false);

  } else {
    $("#inactivos").prop("checked", false);
    $("#todos").prop("checked", false);
    $("#activos").prop("checked", false);

  }
}




function abrir_modal_general(url) {

  $("#edicion").load(url, function () {
    $(this).modal("show");

  });


}

function actulizar_eliminar(url, accion, docente) {

  if (accion == "habilitar") {
    swal({
      title: "¿Está segur@?",
      text: "Va a habilitar a " + docente,
      icon: "warning",
      buttons: true,
      dangerMode: true,
    })
      .then((willDelete) => {
        if (willDelete) {
          var formData = new FormData();
          formData.append('csrfmiddlewaretoken', '{{ csrf_token }}')
          formData.append('accion', accion)
          var request = $.ajax({
            type: "POST",
            url: url,
            data: formData,
            success: function (response) {
              swal("El docente ha sido habilitado correctamente!", {
                icon: "success",
              });
              window.location = "{% url 'academico_app:list-teacher' %}";
            }
          });

        }
      });

  } else {
    swal({
      title: "¿Está segur@?",
      text: "Va a inhabilitar a " + docente,
      icon: "warning",
      buttons: true,
      dangerMode: true,
    })
      .then((willDelete) => {
        if (willDelete) {
          var formData = new FormData();
          formData.append('csrfmiddlewaretoken', '{{ csrf_token }}')
          formData.append('accion', accion)
          var request = $.ajax({
            type: "POST",
            url: url,
            data: formData,
            success: function (response) {
              swal("El docente ha sido inhabilitado correctamente!", {
                icon: "success",
              });
              window.location = "{% url 'academico_app:list-teacher' %}";
            }
          });

        }
      });

  }
}


function abrir_modal_deluxe(url, corte, asignatura) {

  $("#edicion").load(url, function () {
    $(this).modal("show");
    document.getElementById("corteFull").value = corte;
    document.getElementById("asignatura").value = asignatura;

  });


}

function mostrarOkInformes() {
  Swal.fire({
    "title": "Excelente!",
    "text": "El informe ha sido generado",
    "icon": "success",
    "timer": 10000,
  })
}

function mostrarOkpayments() {
  Swal.fire({
    "title": "Excelente!",
    "text": "Pago registrado exitosamente",
    "icon": "success",
    "timer": 10000,
  })
}

function mostrarOk() {
  Swal.fire({
    "title": "Excelente!",
    "text": "El registro ha sido exitoso",
    "icon": "success",
    "timer": 10000,
  })
}

function mostrarError() {
  Swal.fire({
    "title": "Aún falta algo",
    "text": "Verifica las indicaciones en la parte superior del formulario.",
    "icon": "error"
  })
}

function mostrarErrorblanco() {
  Swal.fire({
    "title": "Aún falta algo",
    "text": "No pueden haber valores en blanco ni ceros",
    "icon": "error"
  })
}

function mostrarErrorvacio() {
  Swal.fire({
    "title": "Aún falta algo",
    "text": "Por favor cargue algo, el formulario no puede estar vacío.",
    "icon": "error"
  })
}


function noPuntoComa(event) {

  var e = event || window.event;
  var key = e.keyCode || e.which;

  if (key === 110 || key === 190 || key === 188) {

    e.preventDefault();
  }
}

function getPensum() {
  var estadoId = $("#carrera").val();
  if (estadoId) {
    // Eliminamos las opciones anteriores del select
    $("#pensum_asig").html("");
    var request = $.ajax({
      type: "GET",
      url: "{% url 'academico_app:update-pensum' %}",
      data: {
        estado_id: estadoId,
      },
      success: function (response) {
        $("#pensum_asig").html(response.malla);
      },
    });
    request.done(function (response) {
      // Agregamos los resultados al select
      $("#pensum_asig").html(response.malla);
    });
  } else {
    $("#pensum_asig").html(
      "<option value='' selected='selected'>---------</option>"
    );
  }
}

function mostrarErroresDetalle(error) {
  const array1 = ['tDocument', 'cedula', 'codigo', 'nombre', 'nombres', 'apellidos', 'nacionalidad', 'telefono', 'sexo',
    'direccion', 'nacimiento', 'carrera', 'pensum_asig', 'email', 'sede', 'periodo_matriculado',
    'username', 'nombre_acudiente', 'apellidos_acudiente', 'telefono_acudiente', 'cedula_acudiente', 'consecutivo', 'cedulaAcudiente',
    "document", "fotos"];

  for (const i in array1) {
    const lista = array1[i]
    $('div[class="' + lista + '"]').html("");
  }

  for (const i in error.responseJSON.error) {
    const lista = i
    let errores = "";
    errores += '<div class ="alert alert-danger" <strong>' + error.responseJSON.error[i] + '</strong></div>'
    $('div[class="' + lista + '"]').append(errores);
  }
}


function mostrarErroresCreacion(errores) {

  $("#errores").html("");
  let error = "";

  let datos = errores.responseJSON;

  for (let index = 0; index < datos.length; index++) {
    const element = datos[index];
    console.log(errores.responseJSON[0].error)
    $("#errores").append(`<div class ="alert alert-danger" <strong>${element.error}</strong></div>`);
  }

}

function mostrarErroresCreacionEditar(errores) {

  const array1 = ['tDocument', 'cedula', 'codigo', 'nombre', 'nombres', 'apellidos', 'nacionalidad', 'telefono', 'sexo',
    'direccion', 'nacimiento', 'carrera', 'pensum_asig', 'email', 'sede', 'periodo_matriculado',
    'username', 'nombre_acudiente', 'apellidos_acudiente', 'telefono_acudiente', 'cedula_acudiente', "password1", "password2",
    "tipe", "anio", "periodo", 'programa_name', "aceptado", "matricula", "cuotas", "cuota_valor", "nombre_materia", "programa",
    "tarea", "observacion"
  ];

  for (const i in array1) {
    const lista = array1[i]
    $('div[class="' + lista + '"]').html("");
  }

  let error = "";
  for (let i in errores.responseJSON[0].error) {

    $('div[class="' + i + '"]').append('<div class ="alert alert-danger" <strong>' + errores.responseJSON[0].error[i][0] + '</strong></div>');

  }

}

function sendUser() {
  var serializedData = $("#dataGeneralForm").serialize();
  if (serializedData) {

    var request = $.ajax({
      type: "POST",
      url: "{% url 'academico_app:create-teacher' %}",
      data: serializedData,
      success: function (response) {
        $("#edicion").modal("hide");
        window.location = "{% url 'academico_app:list-teacher' %}";
        Swal.fire({
          "title": "Excelente!",
          "text": "El registro ha sido exitoso",
          "icon": "success"
        })

      },
      error: function (error) {
        mostrarErroresCreacion(error);
        Swal.fire({
          "title": "Aun falta algo",
          "text": "Verifica las indicaciones en la parte superior del formulario.",
          "icon": "error"
        })
      }
    });
  }
}





function abrir_modal_crearEvent(url) {
  $("#exampleModalScrollable").load(url.url, function () {
    $(this).modal("show");
    $('#cierre').click(function () {
      $("#exampleModalScrollable").modal('hide');
    });
    $('#cierre2').click(function () {
      $("#exampleModalScrollable").modal('hide');
    });

    if (url.fecha === undefined) {
      $('#FechaInicio').val(url.fecha_inicio);
      $('#FechaFin').val(url.fecha_fin);
      $('#HoraInicio').val(url.Hora_inicio);


    } else {
      $('#FechaInicio').val(url.fecha);
      $('#FechaFin').val(url.fecha);

    }



  });

}




// Esta función modifica el css del menú, teniendo en cuenta el url actual

$(document).ready(function () {
  var $ = jQuery.noConflict();
  var tabla = $('#table_general').DataTable({


    language: {
      "decimal": "",
      "emptyTable": "No hay información",
      "info": "Mostrando _START_ a _END_ de _TOTAL_ Registros",
      "infoEmpty": "Mostrando 0 to 0 of 0 Registros",
      "infoFiltered": "(Filtrado de _MAX_ total entradas)",
      "infoPostFix": "",
      "thousands": ",",
      "lengthMenu": "Items por rango: _MENU_",
      "loadingRecords": "Cargando...",
      "processing": "Procesando...",
      "search": "Buscar:",
      "zeroRecords": "Sin resultados encontrados",
      "paginate": {
        "first": "Primero",
        "last": "Ultimo",
        "next": "Siguiente",
        "previous": "Anterior"
      }
    }

  });
})


$(document).ready(function () {
  var $ = jQuery.noConflict();
  var tabla = $('#table_id2').DataTable({


    language: {
      "decimal": "",
      "emptyTable": "No hay información",
      "info": "Mostrando _START_ a _END_ de _TOTAL_ Registros",
      "infoEmpty": "Mostrando 0 to 0 of 0 Registros",
      "infoFiltered": "(Filtrado de _MAX_ total entradas)",
      "infoPostFix": "",
      "thousands": ",",
      "lengthMenu": "Items por rango: _MENU_",
      "loadingRecords": "Cargando...",
      "processing": "Procesando...",
      "search": "Buscar:",
      "zeroRecords": "Sin resultados encontrados",
      "paginate": {
        "first": "Primero",
        "last": "Ultimo",
        "next": "Siguiente",
        "previous": "Anterior"
      }
    },
    "columns": [
      { "width": "4%", "className": 'dt-body-center' },
      null,
      null,
      null,
      null,
    ],

  });
})

$(document).ready(function () {
  var $ = jQuery.noConflict();
  var tabla = $('#table_id3').DataTable({

    language: {
      "decimal": "",
      "emptyTable": "No hay información",
      "info": "Mostrando _START_ a _END_ de _TOTAL_ Registros",
      "infoEmpty": "Mostrando 0 to 0 of 0 Registros",
      "infoFiltered": "(Filtrado de _MAX_ total entradas)",
      "infoPostFix": "",
      "thousands": ",",
      "lengthMenu": "Items por rango: _MENU_",
      "loadingRecords": "Cargando...",
      "processing": "Procesando...",
      "search": "Buscar:",
      "zeroRecords": "Sin resultados encontrados",
      "paginate": {
        "first": "Primero",
        "last": "Ultimo",
        "next": "Siguiente",
        "previous": "Anterior"
      }
    },
    "columns": [
      { "width": "4%", "className": 'dt-body-center' },
      null,
      null,
      null,
      null,
      null,
      null,
    ],

  });




})

$(document).ready(function () {
  var $ = jQuery.noConflict();
  var tabla = $('#table_id4').DataTable({

    order: [[0, 'desc'], [4, 'desc']],

    language: {
      "decimal": "",
      "emptyTable": "No hay información",
      "info": "Mostrando _START_ a _END_ de _TOTAL_ Registros",
      "infoEmpty": "Mostrando 0 to 0 of 0 Registros",
      "infoFiltered": "(Filtrado de _MAX_ total entradas)",
      "infoPostFix": "",
      "thousands": ",",
      "lengthMenu": "Items por rango: _MENU_",
      "loadingRecords": "Cargando...",
      "processing": "Procesando...",
      "search": "Buscar:",
      "zeroRecords": "Sin resultados encontrados",
      "paginate": {
        "first": "Primero",
        "last": "Ultimo",
        "next": "Siguiente",
        "previous": "Anterior"
      }
    },
    "columns": [
      { "width": "4%", "className": 'dt-body-center' },
      null,
      null,
      null,
      { "width": "2%", "className": 'dt-body-center' },
      { "width": "2%", "className": 'dt-body-center' },
    ],


  });
})

$(document).ready(function () {
  var $ = jQuery.noConflict();
  var tabla = $('#table_idinf').DataTable({

    language: {
      "decimal": "",
      "emptyTable": "No hay información",
      "info": "Mostrando _START_ a _END_ de _TOTAL_ Registros",
      "infoEmpty": "Mostrando 0 to 0 of 0 Registros",
      "infoFiltered": "(Filtrado de _MAX_ total entradas)",
      "infoPostFix": "",
      "thousands": ",",
      "lengthMenu": "Items por rango: _MENU_",
      "loadingRecords": "Cargando...",
      "processing": "Procesando...",
      "search": "Buscar:",
      "zeroRecords": "Sin resultados encontrados",
      "paginate": {
        "first": "Primero",
        "last": "Ultimo",
        "next": "Siguiente",
        "previous": "Anterior"
      }
    },
    "columns": [
      null,
      null,
    ],

  });

})











