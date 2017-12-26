function attach() {
$(".side_banner__container").stick_in_parent({container: $("#topResults"), offset_top: 0});
}

$(document.body).on("click", ".detach", function(e) {
$(".side_banner__container").trigger("sticky_kit:detach");
});

$(document.body).on("click", ".attach", attach);
attach();
