var ASB = document.getElementById("ASB");
var Form = document.getElementById("Form");

/*====================Form Functions====================*/
ASB.style.display="none";
function show()
{
    ASB.style.display="none";
    Form.style.display="block";
}

function hide()
{
    ASB.style.display="block";
    Form.style.display="none";
}

var Label = document.getElementsByTagName('label');
Label[0].innerHTML+=":";
Label[1].innerHTML+=":";
Label[2].innerHTML+=":";

var Input = document.getElementsByTagName('input')
Input[1].placeholder = 'Enter Event Name';

var Textarea = document.getElementsByTagName('textarea')
Textarea[0].placeholder = "Describe Event Here...............";
/*====================Form Functions====================*/
