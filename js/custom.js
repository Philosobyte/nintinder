$(document).ready(function() {
    $('#header-col-1 > button').click(function() {
        scrollLock();
        $('#sidebar')
            .sidebar({context: $("#main-content")})
            .sidebar('setting', 'transition', 'overlay')
            .sidebar('toggle')
    })

});

/* 
Disclaimer: Semantic-UI has a scroll lock feature for the sidebar but I can't get it to work so this is my alternative

TL:DR: A simple function that locks and unlocks the scrolling of the page.

The function works by first getting the body element of the webpage and setting it to a variable called 'body'. We then check to see if the page is lock or not locked. If it a page is locked overflow should set to hidden and if it is unlock it should be set to empty string
*/
function scrollLock(){
  var body = document.getElementsByTagName("body")[0]
  if(body.style.overflow == 'hidden'){
    body.style.overflow = ''
  }else{
    body.style.overflow = 'hidden'
  }
  console.log(body.style.overflow)
}