var Gallery =  document.getElementById("Gallery");
var AUOC = document.getElementById("AUOC");
var Copyright = document.getElementById("Copyright");

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
    Gallery.style.backgroundColor="black";
    AUOC.style.backgroundColor="#111";
    Copyright.style.backgroundColor="black";

    document.getElementById("navbar_brand_span").style.color="white";
    for(i=0; i<=6; i++)
    {
    header_nav_link[i].style.color="white";
    }
    document.getElementsByClassName("selected")[0].style.color="rgb(0, 0, 187)";

    document.getElementById("Moon").hidden=true;
    document.getElementById("Sun").hidden=false;
    document.getElementById("Sun").style.color="white";
}

function light()
{
    localStorage.setItem('theme', 'false')

    Header.style.backgroundColor="white";
    Gallery.style.backgroundColor="white";
    AUOC.style.backgroundColor="black";
    Copyright.style.backgroundColor="#111";

    document.getElementById("navbar_brand_span").style.color="black";
    for(i=0; i<=6; i++)
    {
    header_nav_link[i].style.color="black";
    }
    document.getElementsByClassName("selected")[0].style.color="rgb(0, 0, 187)";

    document.getElementById("Moon").hidden=false;
    document.getElementById("Sun").hidden=true;
    document.getElementById("Sun").style.color="black";
}
/*====================Theme Functions====================*/