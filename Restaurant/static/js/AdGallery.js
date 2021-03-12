var AGB = document.getElementById("AGB");
var Form = document.getElementById("Form");

/*====================Form Functions====================*/
AGB.style.display="none";
function show()
{
    AGB.style.display="none";
    Form.style.display="block";
}

function hide()
{
    AGB.style.display="block";
    Form.style.display="none";
}

var Label = document.getElementsByTagName('label');
Label[0].innerHTML+=":";
Label[1].innerHTML+=":";

var Input = document.getElementsByTagName('input')
Input[1].placeholder = 'Enter Picture Name';
/*====================Form Functions====================*/
