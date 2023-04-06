function getParameterByName(name, url) {
    if (!url) url = window.location.href;
    name = name.replace(/[\[\]]/g, '\\$&');
    var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
        results = regex.exec(url);
    if (!results) return null;
    if (!results[2]) return '';
    return decodeURIComponent(results[2].replace(/\+/g, ' '));
}

$(document).ready(function() {
    var jobId = getParameterByName('job_id');

    $.ajax({
        url: '/get_job',
        type: 'GET',
        dataType: 'json',
        data: {job_id: jobId},
        success: function(data) {
            // Populate slideshow
            for (var i = 0; i < data.images.length; i++) {
                var slide = $('<div>').addClass('slide');
                $('<img>').attr('src', data.images[i]).appendTo(slide);
                slide.appendTo('.slideshow-container');
            }

            // Display job description
            $('#job-description').text(data.description);
        }
    });
});
