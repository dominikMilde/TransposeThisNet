$(document).ready(function() {
    if (window.location.pathname === '/'){
        $("#mi1").addClass("active");
    }
    if (window.location.pathname === '/info'){
        //$("#mi2").classList.add("active");
        $("#mi2").addClass("active");
    }
    if (window.location.pathname === '/download'){
        $("#mi3").addClass("active");
    }
    if (window.location.pathname === '/report'){
        $("#mi4").addClass("active");
    }
});