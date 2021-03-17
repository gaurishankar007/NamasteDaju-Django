var Stories = document.getElementById("Stories");
var Sp = document.getElementsByClassName("Sp");
var Sh2 = document.getElementsByClassName("Sh2");
var Sh4 = document.getElementsByClassName("Sh4");
var Sb1 = document.getElementsByClassName("Sb1");
var Sb2 = document.getElementsByClassName("Sb2");
var AUOC = document.getElementById("AUOC");
var Copyright = document.getElementById("Copyright");

for(i=0; i<Sp.length; i++)
{
    Sp[i].style.display="none";
}
for(i=0; i<Sb2.length; i++)
{
    Sb2[i].style.display="none";
}

/*====================Theme Functions====================*/
function dark()
{
    Header.style.backgroundColor="black";
    Stories.style.backgroundColor="black";
    AUOC.style.backgroundColor="#111";
    Copyright.style.backgroundColor="black";

    document.getElementById("navbar_brand_span").style.color="white";
    for(i=0; i<=6; i++)
    {
    header_nav_link[i].style.color="white";
    }
    document.getElementsByClassName("selected")[0].style.color="rgb(0, 0, 187)";

    for(i=0; i<Sh2.length; i++)
    {
        Sh2[i].style.color="white";
    }
    for(i=0; i<Sh4.length; i++)
    {
        Sh4[i].style.color="white";
    }
    for(i=0; i<Sp.length; i++)
    {
        Sp[i].style.color="white";
    }

    document.getElementById("Moon").hidden=true;
    document.getElementById("Sun").hidden=false;
    document.getElementById("Sun").style.color="white";
}

function light()
{
    Header.style.backgroundColor="white";
    Stories.style.backgroundColor="white";
    AUOC.style.backgroundColor="black";
    Copyright.style.backgroundColor="#111";

    document.getElementById("navbar_brand_span").style.color="black";
    for(i=0; i<=6; i++)
    {
    header_nav_link[i].style.color="black";
    }
    document.getElementsByClassName("selected")[0].style.color="rgb(0, 0, 187)";

    for(i=0; i<Sh2.length; i++)
    {
        Sh2[i].style.color="black";
    }
    for(i=0; i<Sh4.length; i++)
    {
        Sh4[i].style.color="black";
    }
    for(i=0; i<Sp.length; i++)
    {
        Sp[i].style.color="black";
    }

    document.getElementById("Moon").hidden=false;
    document.getElementById("Sun").hidden=true;
    document.getElementById("Sun").style.color="black";
}
/*====================Theme Functions====================*/

/*====================Reading Functions====================*/
function more(current)
{
    for (var i = 0; i < Sb1.length; i++) {
        if (Sb1[i] === current)
        {
            Sp[i].style.display="block";
            Sb1[i].style.display="none";
            Sb2[i].style.display="block";
        }
    }    
}
function less(current)
{
    for (var i = 0; i < Sb2.length; i++) {
        if (Sb2[i] === current)
        {
            Sp[i].style.display="none";
            Sb1[i].style.display="block";
            Sb2[i].style.display="none";
        }
    } 
}
/*====================Reading Functions====================*/


