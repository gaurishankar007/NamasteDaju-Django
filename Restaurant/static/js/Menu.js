var AUOC = document.getElementById("AUOC");
var Copyright = document.getElementById("Copyright");

AUOC.style.backgroundColor="black";
Copyright.style.backgroundColor="#111";
/*====================Theme Functions====================*/
function dark()
{
    theme = "dark";

    Header.style.backgroundColor="black";
    Form.style.backgroundColor="#111";
    AUOC.style.backgroundColor="#111";
    Copyright.style.backgroundColor="black";

    document.getElementById("Moon").hidden=true;
    document.getElementById("Sun").hidden=false;
    document.getElementById("Sun").style.color="white";
}

function light()
{
    theme = "light";

    Header.style.backgroundColor="white";
    Form.style.backgroundColor="white";
    AUOC.style.backgroundColor="black";
    Copyright.style.backgroundColor="#111";

    document.getElementById("Moon").hidden=false;
    document.getElementById("Sun").hidden=true;
    document.getElementById("Sun").style.color="black";
}
/*====================Theme Functions====================*/