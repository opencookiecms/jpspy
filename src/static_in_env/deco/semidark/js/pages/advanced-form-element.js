//[advanced form element Javascript]


$(function() {
    "use strict";

    //Initialize Select2 Elements
    $('.select2').select2({
        minimumResultsForSearch: Infinity
    });

    $('.select231').select2({
        minimumResultsForSearch: Infinity,
        width: 500
    });

    $('.select232').select2({
        minimumResultsForSearch: Infinity,
        width: 500
    });

    $('.select233').select2({
        minimumResultsForSearch: Infinity,
        width: 500
    });

    $('.select221').select2({
        minimumResultsForSearch: Infinity
    });

    $('.select21').select2({
        minimumResultsForSearch: Infinity,
        width: 500
    });
    $('.select22').select2({
        minimumResultsForSearch: Infinity,
        width: 500
    });
    $('.select23').select2({
        minimumResultsForSearch: Infinity,
        width: 500
    });
    $('.select24').select2({
        minimumResultsForSearch: Infinity,
        width: 500
    });
    $('.select25').select2({
        minimumResultsForSearch: Infinity,
        width: 500
    });
    $('.select26').select2({
        minimumResultsForSearch: Infinity,
        width: 400
    });

    $('.select27').select2({
        minimumResultsForSearch: Infinity,
        width: 300
    });
    //Datemask dd/mm/yyyy
    $('#datemask').inputmask('dd/mm/yyyy', { 'placeholder': 'dd/mm/yyyy' });
    //Datemask2 mm/dd/yyyy
    $('#datemask2').inputmask('mm/dd/yyyy', { 'placeholder': 'mm/dd/yyyy' });
    //Money Euro
    $('[data-mask]').inputmask();


    //iCheck for checkbox and radio inputs
    $('.ichack-input input[type="checkbox"].minimal, .ichack-input input[type="radio"].minimal').iCheck({
        checkboxClass: 'icheckbox_minimal-blue',
        radioClass: 'icheckbox_minimal-blue'
    });
    //Red color scheme for iCheck
    $('.ichack-input input[type="checkbox"].minimal-red, .ichack-input input[type="radio"].minimal-red').iCheck({
        checkboxClass: 'icheckbox_minimal-red',
        radioClass: 'iradio_minimal-red'
    });
    //Flat red color scheme for iCheck
    $('.ichack-input input[type="checkbox"].flat-red, .ichack-input input[type="radio"].flat-red').iCheck({
        checkboxClass: 'icheckbox_flat-green',
        radioClass: 'iradio_flat-green'
    });

    //Colorpicker
    $('.my-colorpicker1').colorpicker();
    //color picker with addon
    $('.my-colorpicker2').colorpicker();

    //Timepicker
    $('.timepicker').timepicker({
        showInputs: false
    });

    //Bootstrap-TouchSpin
    $(".vertical-spin").TouchSpin({
        verticalbuttons: true,
        verticalupclass: 'ti-plus',
        verticaldownclass: 'ti-minus'
    });
    var vspinTrue = $(".vertical-spin").TouchSpin({
        verticalbuttons: true
    });
    if (vspinTrue) {
        $('.vertical-spin').prev('.bootstrap-touchspin-prefix').remove();
    }
    $("input[name='demo1']").TouchSpin({
        min: 0,
        max: 100,
        step: 0.1,
        decimals: 2,
        boostat: 5,
        maxboostedstep: 10,
        postfix: '%'
    });
    $("input[name='demo2']").TouchSpin({
        min: -1000000000,
        max: 1000000000,
        stepinterval: 50,
        maxboostedstep: 10000000,
        prefix: '$'
    });
    $("input[name='demo3']").TouchSpin();
    $("input[name='demo3_1']").TouchSpin({
        initval: 40
    });
    $("input[name='demo4']").TouchSpin({
        prefix: "pre",
        postfix: "post"
    });

});


$(function() {
    'use strict'
    // Datepicker
    $('.fc-datepicker').datepicker({
        showOtherMonths: true,
        selectOtherMonths: true
    });

    $('#datepickerNoOfMonths').datepicker({
        showOtherMonths: true,
        selectOtherMonths: true,
        numberOfMonths: 2
    });

});