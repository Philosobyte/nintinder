$(document).ready(function() {
    $('#header-col-1 > button').click(function() {
        $('#sidebar')
            .sidebar('setting', 'scrollLock', false)
            .sidebar('setting', {
                dimPage: false,
                exclusive: true,
                transition: "overlay"
            })
            .sidebar('setting', 'transition', 'overlay')
            .sidebar('toggle')
    })

});
