$(document).ready(function () {
    $('.fold-button').on('click', function () {
        var button = $(this);
        var post = button.parents('.one-post');

        if (post.hasClass('folded')) {
            post.removeClass('folded');
            button.text('свернуть');
        } else {
            post.addClass('folded');
            button.text('развернуть');
        }
    });

    $('.one-post').hover(
        function (event) {
            $(event.currentTarget)
                .find('.one-post-shadow')
                .stop(true)
                .animate({ opacity: '0.1' }, 300);
        },
        function (event) {
            $(event.currentTarget)
                .find('.one-post-shadow')
                .stop(true)
                .animate({ opacity: '0' }, 300);
        }
    );

    $('.logo').hover(
        function () {
            $(this).stop(true).animate({ width: '338px' }, 300);
        },
        function () {
            $(this).stop(true).animate({ width: '318px' }, 300);
        }
    );
});
