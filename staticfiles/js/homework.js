document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.readable-font');
    const submitButton = form.querySelector('.btn-submit');
    const submissionModal = new bootstrap.Modal(document.getElementById("submissionModal"));
    
    // Prevent default form submission
    form.onsubmit = function(e) {
        e.preventDefault();
    };
    
    // Handle initial submission click
    submitButton.addEventListener('click', function(e) {
        if (form.checkValidity()) {
            submissionModal.show();
            }
        else {
            alert("Please fill out all required fields.");
        }
    });
    
    // Handle modal confirmation
    document.getElementById('submissionConfirm').addEventListener('click', function(e) {
        form.submit();
    });
});