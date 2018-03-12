$(document).ready(function() {
    $('#header-col-1 > button').click(function() {
        $('#sidebar')
            .sidebar({
              context: $("#main-content")
            })
            .sidebar('setting', 'transition', 'overlay')
            .sidebar('toggle')
    })

});
