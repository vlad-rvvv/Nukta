$(document).ready(function () {
    $(".right-arrow").click(function (event) {
        $(".right-arrow").toggleClass("disabled");
        $(".left-arrow").toggleClass("disabled");
        $(".current").toggleClass("disable");
        $(".next").toggleClass("disable");
        $(".dates_next").toggleClass("disable");
        $(".dates").toggleClass("disable");
    });
    $(".left-arrow").click(function (event) {
        $(".right-arrow").toggleClass("disabled");
        $(".left-arrow").toggleClass("disabled");
        $(".current").toggleClass("disable");
        $(".next").toggleClass("disable");
        $(".dates_next").toggleClass("disable");
        $(".dates").toggleClass("disable");
    });
})