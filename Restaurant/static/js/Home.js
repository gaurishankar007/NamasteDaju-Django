var About = document.getElementById("About");
var AUOC = document.getElementById("AUOC");
var Copyright = document.getElementById("Copyright");
var Services = document.getElementById("Services");
var Chef = document.getElementById("Chef");
var CustomerReview = document.getElementById("CustomerReview");
var Customers = document.getElementById("Customers");

var Ssp = document.getElementsByClassName('Ssp');
var Sh3 = document.getElementsByClassName('Sh3');
var Sp = document.getElementsByClassName('Sp');
for(i=0; i<=4; i++)
{
    Ssp[i].style.color="black";
    Sh3[i].style.color="black";
    Sp[i].style.color="#696969";
}

var Ch3 = document.getElementsByClassName('Ch3');
var Cp = document.getElementsByClassName('Cp');
var Icons = document.getElementsByClassName('Icons');
for(i=0; i<=3; i++)
{
    Ch3[i].style.color="black";
    Cp[i].style.color="#696969";
}
for(i=0; i<=19; i++)
{
    Icons[i].style.color="rgb(0, 0, 187)";
}

var Crp = document.getElementsByClassName('Crp');
var Crh3 = document.getElementsByClassName('Crh3');
for(i=0; i<=11; i++)
{
    Crp[i].style.color="#696969";
}
for(i=0; i<=5; i++)
{
    Crh3[i].style.color="black";
}

Services.style.backgroundColor="#F4F6F6";
Customers.style.backgroundColor="#F4F6F6";

AUOC.style.backgroundColor="black";
Copyright.style.backgroundColor="#111";

var Header = document.getElementById("Header");
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
    About.style.backgroundColor="black";
    AUOC.style.backgroundColor="#111";
    Copyright.style.backgroundColor="black";
    Services.style.backgroundColor="#111";
    Chef.style.backgroundColor="black";
    CustomerReview.style.backgroundColor="black";
    Customers.style.backgroundColor="#111";

    document.getElementById("navbar_brand_span").style.color="white";
    for(i=0; i<=6; i++)
    {
    header_nav_link[i].style.color="white";
    }
    document.getElementsByClassName("selected")[0].style.color="rgb(0, 0, 187)";

    for(i=0; i<=4; i++)
    {
    Ssp[i].style.color="white";
    Sh3[i].style.color="white";
    Sp[i].style.color="#adadad";
    }

    for(i=0; i<=3; i++)
    {
    Ch3[i].style.color="white";
    Cp[i].style.color="#adadad";
    }

    for(i=0; i<=11; i++)
    {
    Crp[i].style.color="#adadad";
    }
    for(i=0; i<=5; i++)
    {
    Crh3[i].style.color="white";
    }

    document.getElementById("ADh1").style.color="white";
    document.getElementById("ADp").style.color="#adadad";

    document.getElementById("Moon").hidden=true;
    document.getElementById("Sun").hidden=false;
    document.getElementById("Sun").style.color="white";
}

function light()
{
    localStorage.setItem('theme', 'false')

    Header.style.backgroundColor="white";
    About.style.backgroundColor="white";
    AUOC.style.backgroundColor="black";
    Copyright.style.backgroundColor="#111";
    Services.style.backgroundColor="#F4F6F6";
    Chef.style.backgroundColor="white";
    CustomerReview.style.backgroundColor="white";
    Customers.style.backgroundColor="#F4F6F6";

    document.getElementById("navbar_brand_span").style.color="black";
    for(i=0; i<=6; i++)
    {
    header_nav_link[i].style.color="black";
    }
    document.getElementsByClassName("selected")[0].style.color="rgb(0, 0, 187)";

    for(i=0; i<=4; i++)
    {
    Ssp[i].style.color="black";
    Sh3[i].style.color="black";
    Sp[i].style.color="#696969";
    }

    for(i=0; i<=3; i++)
    {
    Ch3[i].style.color="black";
    Cp[i].style.color="#696969";
    }

    for(i=0; i<=11; i++)
    {
    Crp[i].style.color="#696969";
    }
    for(i=0; i<=5; i++)
    {
    Crh3[i].style.color="black";
    }

    document.getElementById("ADh1").style.color="black";
    document.getElementById("ADp").style.color="#696969";

    document.getElementById("Moon").hidden=false;
    document.getElementById("Sun").hidden=true;
    document.getElementById("Sun").style.color="black";
}
/*====================Theme Functions====================*/

/*====================RNR Functions====================*/
function animateValue(id, start, end, duration) {
    // assumes integer values for start and end

    var obj = document.getElementById(id);
    var range = end - start;
    // no timer shorter than 50ms (not really visible any way)
    var minTimer = 50;
    // calc step time to show all interediate values
    var stepTime = Math.abs(Math.floor(duration / range));

    // never go below minTimer
    stepTime = Math.max(stepTime, minTimer);

    // get current time and calculate desired end time
    var startTime = new Date().getTime();
    var endTime = startTime + duration;
    var timer;

    function run() {
        var now = new Date().getTime();
        var remaining = Math.max((endTime - now) / duration, 0);
        var value = Math.round(end - (remaining * range));
        obj.innerHTML = value;
        if (value == end) {
            clearInterval(timer);
            }
        }
    timer = setInterval(run, stepTime);
    run();
}

var bol = true;
var ScrollFunc = function() {
    var y=window.scrollY;
    if (y > 1830 && bol==true) {
    bol = false;
    animateValue("YE", 0, 31, 2000);
    animateValue("D", 0, 100, 2000);
    animateValue("HC", 0, 10885, 2000);
    animateValue("S", 0, 105, 2000);
    animateValue("NA", 0, 85, 2000);
    }
    if(y<1830){
    bol = true;
    }
};
window.addEventListener("scroll", ScrollFunc);
/*====================RNR Functions====================*/