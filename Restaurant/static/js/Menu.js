var Menu = document.getElementById("Menu");
var Card = document.getElementsByClassName('card');
var Dh3 = document.getElementsByClassName('Dh3');
var Dp = document.getElementsByClassName('Dp');
var Dh4 = document.getElementsByClassName('Dh4');
var AUOC = document.getElementById("AUOC");
var Copyright = document.getElementById("Copyright");

Menu.style.backgroundColor="white";
AUOC.style.backgroundColor="black";
Copyright.style.backgroundColor="#111";
/*====================Theme Functions====================*/
function dark()
{
    Header.style.backgroundColor="black";
    Form.style.backgroundColor="#111";
    Menu.style.backgroundColor="black";
    AUOC.style.backgroundColor="#111";
    Copyright.style.backgroundColor="black";

    document.getElementById("navbar_brand_span").style.color="white";
    for(i=0; i<=6; i++)
    {
    header_nav_link[i].style.color="white";
    }
    document.getElementsByClassName("selected")[0].style.color="rgb(0, 0, 187)";

    for(i=0; i<=5; i++){
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
    

    document.getElementById("Moon").hidden=true;
    document.getElementById("Sun").hidden=false;
    document.getElementById("Sun").style.color="white";
}

function light()
{
    Header.style.backgroundColor="white";
    Form.style.backgroundColor="white";
    Menu.style.backgroundColor="white";
    AUOC.style.backgroundColor="black";
    Copyright.style.backgroundColor="#111";

    document.getElementById("navbar_brand_span").style.color="black";
    for(i=0; i<=6; i++)
    {
    header_nav_link[i].style.color="black";
    }
    document.getElementsByClassName("selected")[0].style.color="rgb(0, 0, 187)";

    for(i=0; i<=5; i++){
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

    document.getElementById("Moon").hidden=false;
    document.getElementById("Sun").hidden=true;
    document.getElementById("Sun").style.color="black";
}
/*====================Theme Functions====================*/