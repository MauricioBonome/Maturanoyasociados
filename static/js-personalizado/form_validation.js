document.addEventListener("DOMContentLoaded", function() {
    // obtener el formulario
    const form = document.querySelector('form');

    form.addEventListener('submit', function(event) {
        // obtener los campos del formulario
        const firstName = document.getElementById('{{ form.first_name.auto_id }}');
        const lastName = document.getElementById('{{ form.last_name.auto_id }}');
        const email = document.getElementById('{{ form.email.auto_id }}');
        const inquiryType = document.getElementById('{{ form.inquiry_type.auto_id }}');
        const message = document.getElementById('{{ form.message.auto_id }}');
        const documentField = document.getElementById('{{ form.impuesto_inmobiliario.auto_id }}'); // nueva línea

        // validar los campos
        if (!firstName.value) {
            alert('El nombre es requerido.');
            event.preventDefault();
        } else if (!lastName.value) {
            alert('El apellido es requerido.');
            event.preventDefault();
        } else if (!email.value) {
            alert('El correo electrónico es requerido.');
            event.preventDefault();
        } else if (!inquiryType.value) {
            alert('El tipo de consulta es requerido.');
            event.preventDefault();
        } else if (!message.value) {
            alert('El mensaje es requerido.');
            event.preventDefault();
        } else if (!documentField.value) { // nueva línea
            alert('El documento es requerido.'); // nueva línea
            event.preventDefault(); // nueva línea
        }
    });
});
