var PasswordChange =  document.getElementById("PasswordChange");
var Card =  document.getElementById("Card");
var AUOC = document.getElementById("AUOC");
var Copyright = document.getElementById("Copyright");

var Label = document.getElementsByTagName('label');
for(i=0; i<Label.length; i++)
{
    Label[i].innerHTML+=":";
}

var Input = document.getElementsByTagName('input')
Input[1].placeholder = 'Enter Old Password';
Input[2].placeholder = 'Enter New Password';
Input[3].placeholder = 'Enter New Password Again';
/*====================Theme Functions====================*/
function dark()
{
    Header.style.backgroundColor="black";
    PasswordChange.style.backgroundColor="black";
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
    document.getElementById("Moon").hidden=true;
    document.getElementById("Sun").hidden=false;
    document.getElementById("Sun").style.color="white";
}

function light()
{
    Header.style.backgroundColor="white";
    PasswordChange.style.backgroundColor="white";
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

    document.getElementById("Moon").hidden=false;
    document.getElementById("Sun").hidden=true;
    document.getElementById("Sun").style.color="black";
}
/*====================Theme Functions====================*/