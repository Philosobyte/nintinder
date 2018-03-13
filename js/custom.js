$(document).ready(function() {
    $('#header-col-1 > button').click(function() {
        $('#sidebar')
          .sidebar({context: $("#main")})
          .sidebar('setting', 'transition', 'overlay')
          .sidebar('toggle')
        scrollLock();
    })

});

/* 
Disclaimer: Semantic-UI has a scroll lock feature for the sidebar but I can't get it to work so this is my alternative.

TL:DR: A simple function that locks and unlocks the scrolling of the page.
*/
function scrollLock(){
  var body = document.getElementsByTagName('body')[0];
  var pusher = document.getElementById('content');
  if(pusher.className === 'pusher'){
    body.style.overflow = 'hidden';
  }else{
    body.style.overflow = '';
  }
}