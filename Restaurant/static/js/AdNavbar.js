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
