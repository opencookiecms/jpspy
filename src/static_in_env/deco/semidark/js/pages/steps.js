$(".tab-wizard").steps({
    headerTag: "h6",
    bodyTag: "section",
    transitionEffect: "none",
    autoFocus: true,
    enableAllSteps: true,
    titleTemplate: '<span class="number">#index#<\/span> <span class="title">#title#<\/span>',
    titleTemplate: '<span class="step">#index#</span> #title#',
    labels: {
        finish: "Submit"
    },
    onFinished: function(event, currentIndex) {

        $("#form").delay(1000).submit();
        swal("Your Order was save");
    }
});