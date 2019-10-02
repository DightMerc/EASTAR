$(function () {

    $('.menuToggle').on('click', function () {
        $('.menu').slideToggle(300, function () {
            if ($(this).css('display') === "none") {
                $(this).removeAttr('style');
            }
        });

    });

});
var mywindow = $(window);
var mypos = mywindow.scrollTop();
mywindow.scroll(function () {
    if (mywindow.scrollTop() > mypos) {
        $('nav').fadeOut();
    } else {
        $('nav').fadeIn();
    }
    mypos = mywindow.scrollTop();
});