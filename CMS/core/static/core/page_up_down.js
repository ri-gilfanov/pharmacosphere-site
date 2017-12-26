var scroll_position = null;

$('#page_up_down__button').click(function(){
    if ($(document).scrollTop() > 0) {
        scroll_position = $(document).scrollTop();
        $('#page_up_down__button').html('<span class="fa fa-arrow-down"></span> обратно');
        return true;
    } else if (scroll_position > $(document).scrollTop()) {
        $(document).scrollTop(scroll_position);
        $('#page_up_down__button').html('<span class="fa fa-arrow-up"></span> наверх');
        return false;
    };
});

function check_status_button(){
    if ($(document).scrollTop() > 0) {
        scroll_position = null;
        $('#page_up_down__button').html('<span class="fa fa-arrow-up"></span> наверх');
    };
};

$(window).resize(function() {
    check_status_button();
});

$(window).scroll(function() {
    check_status_button();
});