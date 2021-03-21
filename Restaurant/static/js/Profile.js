var Profile =  document.getElementById("Profile");
var CCard =  document.getElementById("CCard");
var Card =  document.getElementById("Card");
var Table =  document.getElementById("Table");
var AUOC = document.getElementById("AUOC");
var Copyright = document.getElementById("Copyright");

var CCh3 = document.getElementsByClassName("CCh3");

var Label = document.getElementsByTagName('label');
for(i=0; i<Label.length; i++)
{
    Label[i].innerHTML+=":";
}

var Input = document.getElementsByTagName('input')
Input[1].placeholder = 'Enter First Name';
Input[2].placeholder = 'Enter Last Name';
Input[3].placeholder = 'Enter Email';
Input[4].placeholder = 'Enter Phone Number';

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
    Profile.style.backgroundColor="black";
    CCard.style.backgroundColor="black";
    Card.style.backgroundColor="black";
    Table.style.backgroundColor="black";
    AUOC.style.backgroundColor="#111";
    Copyright.style.backgroundColor="black";

    document.getElementById("navbar_brand_span").style.color="white";
    for(i=0; i<=6; i++)
    {
    header_nav_link[i].style.color="white";
    }

    for(i=0; i<CCh3.length; i++)
    {
        CCh3[i].style.color="white";
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
    Header.style.backgroundColor="white";
    Profile.style.backgroundColor="white";
    CCard.style.backgroundColor="white";
    Card.style.backgroundColor="white";
    Table.style.backgroundColor="white";
    AUOC.style.backgroundColor="black";
    Copyright.style.backgroundColor="#111";

    document.getElementById("navbar_brand_span").style.color="black";
    for(i=0; i<=6; i++)
    {
    header_nav_link[i].style.color="black";
    }

    for(i=0; i<CCh3.length; i++)
    {
        CCh3[i].style.color="black";
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