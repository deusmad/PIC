$(document).ready(function () {
    var $parallaxElements = $('.icon-for-parallax-first, .icon-for-parallax-second, .icon-for-parallax-third');

    $(window).on('scroll', function () {
        var scrollTop = $(window).scrollTop();

        $('.icon-for-parallax-first').css('transform', 'translateY(' + (scrollTop * 0.35) + 'px)');
        $('.icon-for-parallax-second').css('transform', 'translateY(' + (scrollTop * 0.2) + 'px)');
        $('.icon-for-parallax-third').css('transform', 'translateY(' + (scrollTop * 0.1) + 'px)');
    });
});