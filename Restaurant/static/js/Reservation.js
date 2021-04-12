var Reservation =  document.getElementById("Reservation");
var Card =  document.getElementById("Card");
var AUOC = document.getElementById("AUOC");
var Copyright = document.getElementById("Copyright");

var Label = document.getElementsByTagName('label');
for(i=0; i<Label.length; i++)
{
    Label[i].innerHTML+=":";
}
Label[0].hidden=true;

var users = document.getElementsByTagName('select')[0];
for(i=1; i<users.length; i++){
    if(users.options[i].text==document.getElementById("Username").innerHTML){
        users.options[i].selected = 'selected';
    }
}
users.hidden=true;

var Input = document.getElementsByTagName('input')
Input[1].placeholder = 'Enter First Name';
Input[2].placeholder = 'Enter Last Name';
Input[3].placeholder = 'Enter Email';
Input[4].placeholder = 'Enter Phone Number';

AUOC.style.backgroundColor="black";
Copyright.style.backgroundColor="#111";

var header_nav_link = document.getElementsByClassName('header_nav_link');
document.getElementById("Sun").hidden=true;
if(localStorage.getItem('theme')=='true'){
    dark()
}

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

/*====================Theme Functions====================*/
function dark()
{
    localStorage.setItem('theme', 'true')

    Header.style.backgroundColor="black";
    Reservation.style.backgroundColor="black";
    Card.style.backgroundColor="black";
    AUOC.style.backgroundColor="#111";
    Copyright.style.backgroundColor="black";

    document.getElementById("navbar_brand_span").style.color="white";
    for(i=0; i<=6; i++)
    {
    header_nav_link[i].style.color="white";
    }
    document.getElementsByClassName("selected")[0].style.color="rgb(0, 0, 187)";

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
    Reservation.style.backgroundColor="white";
    Card.style.backgroundColor="white";
    AUOC.style.backgroundColor="black";
    Copyright.style.backgroundColor="#111";

    document.getElementById("navbar_brand_span").style.color="black";
    for(i=0; i<=6; i++)
    {
    header_nav_link[i].style.color="black";
    }
    document.getElementsByClassName("selected")[0].style.color="rgb(0, 0, 187)";

    for(i=0; i<Label.length; i++)
    {
        Label[i].style.color="black";
    }

    document.getElementById("Moon").hidden=false;
    document.getElementById("Sun").hidden=true;
    document.getElementById("Sun").style.color="black";
}
/*====================Theme Functions====================*/