function attach() {
$(".main_page_widgets__block").stick_in_parent({container: $("#topResults"), offset_top: 0});
}

$(document.body).on("click", ".detach", function(e) {
$(".main_page_widgets__block").trigger("sticky_kit:detach");
});

$(document.body).on("click", ".attach", attach);
attach();
