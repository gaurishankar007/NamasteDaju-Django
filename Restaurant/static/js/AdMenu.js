var AMB = document.getElementById("AMB");
var Form = document.getElementById("Form");

/*====================Form Functions====================*/
AMB.style.display="none";
function show()
{
    AMB.style.display="none";
    Form.style.display="block";
}

function hide()
{
    AMB.style.display="block";
    Form.style.display="none";
}

var Label = document.getElementsByTagName('label');
Label[0].innerHTML+=":";
Label[1].innerHTML+=":";
Label[2].innerHTML+=":";
Label[3].innerHTML+=":";
Label[4].innerHTML+=":";

var Input = document.getElementsByTagName('input')
Input[1].placeholder = 'Enter Food Name';
Input[2].placeholder = 'Enter Name of Foods It Contains';
Input[3].placeholder = 'Enter Food Price in Rupees';
/*====================Form Functions====================*/
