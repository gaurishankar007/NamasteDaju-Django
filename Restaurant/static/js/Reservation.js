var Reservation =  document.getElementById("Reservation");
var Card =  document.getElementById("Card");
var AUOC = document.getElementById("AUOC");
var Copyright = document.getElementById("Copyright");

var Label = document.getElementsByTagName('label');
console.log(Label.length)
Label[2].innerHTML+=":";
Label[3].innerHTML+=":";
Label[4].innerHTML+=":";
Label[5].innerHTML+=":";
Label[6].innerHTML+=":";
Label[7].innerHTML+=":";
Label[8].innerHTML+=":";

var Input = document.getElementsByTagName('input')
Input[3].placeholder = 'Enter Name';
Input[4].placeholder = 'Enter Email';
Input[5].placeholder = 'Enter Phone Number';

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
    Header.style.backgroundColor="black";
    Form.style.backgroundColor="#111";
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
    Header.style.backgroundColor="white";
    Form.style.backgroundColor="white";
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