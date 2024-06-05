// scripts.js

document.addEventListener('DOMContentLoaded', function() {
    // Inicialización de Toastify
    Toastify({
        text: "Bienvenido a la aplicación!",
        duration: 3000,
        close: true,
        gravity: "top", // `top` o `bottom`
        position: "right", // `left`, `center` o `right`
        backgroundColor: "linear-gradient(to right, #00b09b, #96c93d)",
    }).showToast();

    // Ejemplo de SweetAlert
    document.querySelectorAll('.btn-delete').forEach(button => {
        button.addEventListener('click', function() {
            const form = this.closest('form');
            Swal.fire({
                title: '¿Estás seguro?',
                text: "No podrás revertir esto!",
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Sí, bórralo!'
            }).then((result) => {
                if (result.isConfirmed) {
                    form.submit();
                }
            });
        });
    });
});

