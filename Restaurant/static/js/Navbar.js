var Header = document.getElementById("Header");
var header_nav_link = document.getElementsByClassName('header_nav_link');

document.getElementById("Sun").hidden=true;

/*====================TopScroll Functions====================*/
function ScrollUp() {
    window.scrollTo({top: 0, behavior: 'smooth'});
}

var myScroll = function() {
    var y=window.scrollY;
    if (y > 150) {
        document.getElementById("TopScroll").style.display="block";
    }
    else
    {
        document.getElementById("TopScroll").style.display="none";
    }
};
window.addEventListener("scroll", myScroll);
/*====================TopScroll Functions====================*/

/*====================Navbar Functions====================*/
var bool = true;
var myScrollFunc = function() {
    var y=window.scrollY;
    if (y > 240 && bool==true) {
        bool = false;
        Header.style.zIndex="2000";
    }
    if(y<240){
        bool = true;
        Header.style.zIndex="0";
    }
};
window.addEventListener("scroll", myScrollFunc);
/*====================Navbar Functions====================*/