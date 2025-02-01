$("#id_subject").change(function () {
    const url = $(this).attr("data-lessons-url");  // get the url of the `load_lessons` view
    const subjectId = $(this).val();  // get the selected subject ID from the HTML input

    $.ajax({  // initialize an AJAX request
        url: url,  // set the url of the request (= /homework/load-lessons/ )
        data: {
            'subject': subjectId  // add the subject id to the GET parameters
        },
        success: function (data) {  // `data` is the return of the `load_lessons` view function
            let html_data = '<option value="">---------</option>';
            data.forEach(function (lesson) {
                html_data += `<option value="${lesson.id}">${lesson.title}</option>`;
            });
            $("#id_lesson").html(html_data);  // replace the contents of the lesson input with the data that came from the server
        }
    });
});