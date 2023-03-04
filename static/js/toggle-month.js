$(document).ready(function () {
    $(".right-arrow").click(function (event) {
        $(".right-arrow").toggleClass("disabled");
        $(".left-arrow").toggleClass("disabled");
    });
    $(".left-arrow").click(function (event) {
        $(".right-arrow").toggleClass("disabled");
        $(".left-arrow").toggleClass("disabled");
    });
})