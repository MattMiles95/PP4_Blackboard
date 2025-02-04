$("#id_subject").change(function() {
    const url = $(this).attr("data-lessons-url");
    const subjectId = $(this).val();
    console.log(`URL: ${url}, Subject ID: ${subjectId}`);
    
    $.ajax({
        url: url,
        data: { 'subject': subjectId },
        success: function(response) {
            console.log('Response:', response);
            
            // Ensure response is parsed as JSON
            let data;
            try {
                data = typeof response === 'string' ? JSON.parse(response) : response;
                
                // Validate data structure
                if (!Array.isArray(data)) {
                    throw new Error('Invalid response format: expected array of lessons');
                }
                
                // Build select options
                let html_data = '<option value="">---------</option>';
                data.forEach(function(lesson) {
                    if (!lesson.id || !lesson.title) {
                        console.warn('Invalid lesson object:', lesson);
                        return;
                    }
                    html_data += `<option value="${lesson.id}">${lesson.title}</option>`;
                });
                
                $("#id_lesson").html(html_data);
            } catch (error) {
                console.error('Error processing lessons:', error);
                $("#id_lesson").html('<option>Error loading lessons</option>');
            }
        },
        error: function(xhr, status, error) {
            console.error('AJAX Error:', error);
            const errorMessage = xhr.responseJSON?.error || 
                               xhr.responseText || 
                               'Unknown error occurred';
            $("#id_lesson").html(`<option>Error: ${errorMessage}</option>`);
        }
    });
});