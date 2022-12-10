$(window).scroll(function() {

    if ($(this).scrollTop() < 1){  

        $('.header').addClass("fixed");
        $('.nav__item').addClass("fixed_item");
        $('.phone__number').addClass("fixed_item");
        $('.phone__text').addClass("fixed_item");
        $('.phone__holder').addClass("fixed_item");

    }  else{

        $('.header').removeClass("fixed");
        $('.nav__item').removeClass("fixed_item");
        $('.phone__number').removeClass("fixed_item");
        $('.phone__text').removeClass("fixed_item");
        $('.phone__holder').removeClass("fixed_item");
    }

});