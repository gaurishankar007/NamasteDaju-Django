var Register =  document.getElementById("Register");
var Card =  document.getElementById("Card");
var AUOC = document.getElementById("AUOC");
var Copyright = document.getElementById("Copyright");
var LI = document.getElementsByTagName("li");

var Label = document.getElementsByTagName('label');
console.log(Label.length)
Label[0].innerHTML+=":";
Label[1].innerHTML+=":";
Label[2].innerHTML+=":";

var Input = document.getElementsByTagName('input')
Input[1].placeholder = 'Enter Username';
Input[2].placeholder = 'Enter Password';
Input[3].placeholder = 'Enter Password Again';

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
    Register.style.backgroundColor="black";
    Card.style.backgroundColor="black";
    AUOC.style.backgroundColor="#111";
    Copyright.style.backgroundColor="black";

    document.getElementById("navbar_brand_span").style.color="white";
    for(i=0; i<=6; i++)
    {
    header_nav_link[i].style.color="white";
    }

    for(i=0; i<Label.length; i++)
    {
        Label[i].style.color="white";
    }

    for(i=0; i<LI.length; i++)
    {
        LI[i].style.color="white";
    }

    document.getElementById("Moon").hidden=true;
    document.getElementById("Sun").hidden=false;
    document.getElementById("Sun").style.color="white";
}

function light()
{
    localStorage.setItem('theme', 'false')
    
    Header.style.backgroundColor="white";
    Register.style.backgroundColor="white";
    Card.style.backgroundColor="white";
    AUOC.style.backgroundColor="black";
    Copyright.style.backgroundColor="#111";

    document.getElementById("navbar_brand_span").style.color="black";
    for(i=0; i<=6; i++)
    {
    header_nav_link[i].style.color="black";
    }

    for(i=0; i<Label.length; i++)
    {
        Label[i].style.color="black";
    }

    for(i=0; i<LI.length; i++)
    {
        LI[i].style.color="black";
    }

    document.getElementById("Moon").hidden=false;
    document.getElementById("Sun").hidden=true;
    document.getElementById("Sun").style.color="black";
}
/*====================Theme Functions====================*/