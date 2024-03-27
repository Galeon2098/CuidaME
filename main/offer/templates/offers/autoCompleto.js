$(document).ready(function() {
    // Lista de poblaciones disponibles
    var poblaciones = [
        {% for choice_value, choice_label in form.poblacion.field.choices %}
            "{{ choice_label }}",
        {% endfor %}
    ];

    // Función para filtrar las poblaciones disponibles según la entrada del usuario
    $("#poblacion").on("input", function() {
        var input = $(this).val().toLowerCase();
        var output = [];
        poblaciones.forEach(function(poblacion) {
            if (poblacion.toLowerCase().indexOf(input) !== -1) {
                output.push(poblacion);
            }
        });
        // Actualizar las opciones de autocompletado
        var datalist = $("#poblacion-list");
        datalist.empty();
        output.forEach(function(poblacion) {
            datalist.append("<option value='" + poblacion + "'>");
        });
    });
});