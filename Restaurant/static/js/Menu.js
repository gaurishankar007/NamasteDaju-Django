var Menu = document.getElementById("Menu");
var Card = document.getElementsByClassName('card');
var Form = document.getElementById("Form");
var Dh3 = document.getElementsByClassName('Dh3');
var Dp = document.getElementsByClassName('Dp');
var Dh4 = document.getElementsByClassName('Dh4');
var Da = document.getElementsByClassName('Da');
var AUOC = document.getElementById("AUOC");
var Copyright = document.getElementById("Copyright");
var Label = document.getElementsByTagName('label');

for(i=0; i<Da.length; i++){
    Da[i].style.color="black";
    Da[i].style.border="3px solid black";
}

var Label = document.getElementsByTagName('label');
Label[2].innerHTML+=":";
Label[3].innerHTML+=":";
Label[4].innerHTML+=":";
Label[5].innerHTML+=":";
Label[6].innerHTML+=":";

var Input = document.getElementsByTagName('input')
Input[4].placeholder = 'Enter Phone';
Input[6].placeholder = 'Enter Quantity';
Input[7].placeholder = 'Enter Address';

Menu.style.backgroundColor="white";

AUOC.style.backgroundColor="black";
Copyright.style.backgroundColor="#111";

var header_nav_link = document.getElementsByClassName('header_nav_link');
document.getElementById("Sun").hidden=true;
if(localStorage.getItem('theme')=='true'){
    dark()
}

/*====================Theme Functions====================*/
function dark()
{
    localStorage.setItem('theme', 'true')

    Header.style.backgroundColor="black";
    Menu.style.backgroundColor="black";
    AUOC.style.backgroundColor="#111";
    Copyright.style.backgroundColor="black";

    document.getElementById("navbar_brand_span").style.color="white";
    for(i=0; i<=6; i++)
    {
    header_nav_link[i].style.color="white";
    }
    document.getElementsByClassName("selected")[0].style.color="rgb(0, 0, 187)";

    for(i=0; i<=7; i++){
        Card[i].style.backgroundColor="black";
    }

    for(i=0; i<Dh3.length; i++){
        Dh3[i].style.color="white";
    }
    for(i=0; i<Dp.length; i++){
        Dp[i].style.color="white";
    }
    for(i=0; i<Dh4.length; i++){
        Dh4[i].style.color="white";
    }
    for(i=0; i<Da.length; i++){
        Da[i].style.color="white";
        Da[i].style.border="3px solid white";
    }
    
    for(i=0; i<Label.length; i++)
    {
        Label[i].style.color="white";
    }

    document.getElementById("Moon").hidden=true;
    document.getElementById("Sun").hidden=false;
    document.getElementById("Sun").style.color="white";
}

function light()
{
    
    localStorage.setItem('theme', 'false')

    Header.style.backgroundColor="white";
    Menu.style.backgroundColor="white";
    AUOC.style.backgroundColor="black";
    Copyright.style.backgroundColor="#111";

    document.getElementById("navbar_brand_span").style.color="black";
    for(i=0; i<=6; i++)
    {
    header_nav_link[i].style.color="black";
    }
    document.getElementsByClassName("selected")[0].style.color="rgb(0, 0, 187)";

    for(i=0; i<=7; i++){
        Card[i].style.backgroundColor="white";
    }

    for(i=0; i<Dh3.length; i++){
        Dh3[i].style.color="black";
    }
    for(i=0; i<Dp.length; i++){
        Dp[i].style.color="black";
    }
    for(i=0; i<Dh4.length; i++){
        Dh4[i].style.color="black";
    }
    for(i=0; i<Da.length; i++){
        Da[i].style.color="black";
        Da[i].style.border="3px solid black";
    }

    for(i=0; i<Label.length; i++)
    {
        Label[i].style.color="black";
    }

    document.getElementById("Moon").hidden=false;
    document.getElementById("Sun").hidden=true;
    document.getElementById("Sun").style.color="black";
}
/*====================Theme Functions====================*/

/*====================Order Form Functions====================*/
Form.style.display="none";
window.onscroll = function(){Form.style.display="none"}
function show(foodName)
{
    Input[3].value=document.getElementById("Username").innerHTML;
    Input[3].readOnly=true;
    Input[5].value=foodName;
    Input[5].readOnly=true;
    Form.style.display="block";
}

function hide()
{
    Form.style.display="none";
}
/*====================Order Form Functions====================*/

/*====================Phone Number Functions====================*/
function validate(evt) {
    var theEvent = evt || window.event;
  
    // Handle paste
    if (theEvent.type === 'paste') {
        key = event.clipboardData.getData('text/plain');
    } else {
    // Handle key press
        var key = theEvent.keyCode || theEvent.which;
        key = String.fromCharCode(key);
    }
    var regex = /[0-9]|\./;
    if( !regex.test(key) ) {
      theEvent.returnValue = false;
      if(theEvent.preventDefault) theEvent.preventDefault();
    }
}
/*====================Phone Number Functions====================*/
