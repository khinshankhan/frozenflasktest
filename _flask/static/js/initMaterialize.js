//make navbar into sidebar
var elem = document.querySelector('.sidenav');
var instance = new M.Sidenav(elem);

//dropdown menus
$(".dropdown-trigger").dropdown();

//collapsible
$(document).ready(function(){
    $('.collapsible').collapsible();
});
