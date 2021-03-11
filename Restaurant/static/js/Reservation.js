var Reservation =  document.getElementById("Reservation");
var Card =  document.getElementById("Card");
var Label = document.getElementsByTagName("label");
var AUOC = document.getElementById("AUOC");
var Copyright = document.getElementById("Copyright");

var today = new Date();
var day = today.getDate();
var month = today.getMonth()+1; //January is 0 so need to add 1 to make it 1!
var year = today.getFullYear();
if(day<10){
  day='0'+day
} 
if(month<10){
  month='0'+month
} 
today = year+'-'+month+'-'+day;
document.getElementById("date").setAttribute('min', today)

var time_list = ['12:00am','12:30am','1:00am','1:30am','2:00am','2:30am','3:00am','3:30am','4:00am','4:30am','5:00am','5:30am','6:00am','6:30am',
                '7:00am','7:30am','8:00am','8:30am','9:00am','9:30am','10:00am','10:30am','11:00am','11:30am','12:00pm','12:30pm','1:00pm','1:30pm',
                '2:00pm','2:30pm','3:00pm','3:30pm','4:00pm','4:30pm','5:00pm','5:30pm','6:00pm','6:30pm','7:00pm','7:30pm','8:00pm','8:30pm','9:00pm',
                '9:30pm','10:00pm','10:30pm','11:00pm','11:30pm']
for(i=0; i<time_list.length; i++)
{
    document.getElementById('time').innerHTML+="<option value="+time_list[i]+">"+time_list[i]+"</option>";
}
/*====================Theme Functions====================*/
function dark()
{
    Header.style.backgroundColor="black";
    Form.style.backgroundColor="#111";
    Reservation.style.backgroundColor="black";
    Card.style.backgroundColor="black";
    AUOC.style.backgroundColor="#111";
    Copyright.style.backgroundColor="black";

    document.getElementById("navbar_brand_span").style.color="white";
    for(i=0; i<=6; i++)
    {
    header_nav_link[i].style.color="white";
    }
    document.getElementsByClassName("selected")[0].style.color="rgb(0, 0, 187)";

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
    Form.style.backgroundColor="white";
    Reservation.style.backgroundColor="white";
    Card.style.backgroundColor="white";
    AUOC.style.backgroundColor="black";
    Copyright.style.backgroundColor="#111";

    document.getElementById("navbar_brand_span").style.color="black";
    for(i=0; i<=6; i++)
    {
    header_nav_link[i].style.color="black";
    }
    document.getElementsByClassName("selected")[0].style.color="rgb(0, 0, 187)";

    for(i=0; i<Label.length; i++)
    {
        Label[i].style.color="black";
    }

    document.getElementById("Moon").hidden=false;
    document.getElementById("Sun").hidden=true;
    document.getElementById("Sun").style.color="black";
}
/*====================Theme Functions====================*/