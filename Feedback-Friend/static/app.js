document.addEventListener('DOMContentLoaded', function() {
    var registerForm = document.getElementById('registerForm');
    var registerFormFields = registerForm.querySelectorAll('input');
    registerFormFields.forEach(function(field) {
        field.setAttribute('autocomplete', 'off');
    });
});