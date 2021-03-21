var Message = document.getElementById("Message");
var loc = document.getElementById("location");
var Card = document.getElementById("Card");
var AUOC = document.getElementById("AUOC");
var Copyright = document.getElementById("Copyright");

var Label = document.getElementsByTagName('label');
console.log(Label.length)
Label[0].innerHTML+=":";
Label[1].innerHTML+=":";
Label[2].innerHTML+=":";

var Input = document.getElementsByTagName('input')
Input[1].readOnly = true;
Input[1].value = document.getElementById('Username').innerHTML;
Input[2].placeholder = 'Enter Subject'; 

var Textarea = document.getElementsByTagName('textarea')
Textarea[0].placeholder = "Enter Message Here...............";

/*====================Theme Functions====================*/
function dark()
{
    Header.style.backgroundColor="black";
    Message.style.backgroundColor="black";
    loc.style.backgroundColor="black";
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
    Message.style.backgroundColor="white";
    loc.style.backgroundColor="white";
    Card.style.backgroundColor="white"
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