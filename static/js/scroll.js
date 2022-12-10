$(document).ready(function () {
    $('.header__nav a').on('click', function () {

        let href = $(this).attr('href');

        $('html, body').animate({
            scrollTop: $(href).offset().top
        }, {
            duration: 500,   // по умолчанию «400» 
            easing: "linear" // по умолчанию «swing» 
        });

        return false;
    });


    $('.header__right a').on('click', function () {

        let href = $(this).attr('href');

        $('html, body').animate({
            scrollTop: $(href).offset().top
        }, {
            duration: 500,   // по умолчанию «400» 
            easing: "linear" // по умолчанию «swing» 
        });

        return false;
    });
})