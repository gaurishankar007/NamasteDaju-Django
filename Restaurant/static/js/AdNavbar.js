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
    if (y > 150 && bool==true) {
        bool = false;
        Header.style.position="fixed";
        Header.style.top="0";
        Header.style.zIndex="2000";
    }
    if(y<150){
        bool = true;
        Header.style.position="relative";
    }
};
window.addEventListener("scroll", myScrollFunc);
/*====================Navbar Functions====================*/