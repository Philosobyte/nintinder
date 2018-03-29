alert("Fuck")
$(document).ready(function() {
    
    $('#header-col-1 > button').click(function() {
        $('#sidebar')
          .sidebar('setting', 'transition', 'overlay')
          .sidebar('toggle')
        scrollLock();
    })
    
    $('#main-content').click(function(){
      scrollLock();
    })

});

/* 
Disclaimer: Semantic-UI has a scroll lock feature for the sidebar but I can't get it to work so this is my alternative.

TL:DR: A simple function that locks and unlocks the scrolling of the page.

The scrollLock function starts by getting the necessary elements in the webpage. The first is the <body> element which we are setting it to the variable 'body'. We need this elements because we going to set the body's overflow attribute to hidden when the sidebar appears. This will create a 'scroll locking' effect because we are essential cutting the webpage down to fit the height of the current browser. The next element we need is the <div> element with the id 'content' and we are setting this element to the variable 'pusher'. By nature Pusher is a wrapper class that is provided by Semantic UI and from my understand it need for all special animation that occurs. However, the reason behind why we need this element is because when sidebar appears Semantic UI adds a dimmed class to the pusher class.
*/
function scrollLock(){
  var body = document.getElementsByTagName('body')[0];
  var pusher = document.getElementById('main-content');
  if(pusher.className === 'pusher'){
    body.style.overflow = 'hidden';
  }else{
    body.style.overflow = ''
  }
}