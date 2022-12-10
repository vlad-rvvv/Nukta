$(document).ready(function () {
    $(".burger").click(function (event) {
        $(".burger, .header__nav, .phone").toggleClass("active");
    });

    $(".nav a").click(function (event) {
        $(".burger, .nav, .phone").toggleClass("active");
    });
});