var Label = document.getElementsByTagName('label');
console.log(Label.length)
Label[0].innerHTML+=":";
Label[1].innerHTML+=":";
Label[2].innerHTML+=":";

var Input = document.getElementsByTagName('input')
Input[1].placeholder = 'Enter Username';
Input[2].placeholder = 'Enter Password';
Input[3].placeholder = 'Enter Password Again';