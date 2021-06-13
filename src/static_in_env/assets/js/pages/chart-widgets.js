$(function() {
    'use strict'


    $("#barchart3").sparkline([32, 24, 26, 24, 32, 26, 40, 34, 22, 24, 22, 24, 34, 32, 38, 28, 36, 36, 40, 38, 30, 34, 38], {
        type: 'bar',
        height: '45',
        width: '100%',
        barWidth: 6,
        barSpacing: 4,
        barColor: '#f64e60',
    });


    $('.countnm').each(function() {
        $(this).prop('Counter', 0).animate({
            Counter: $(this).text()
        }, {
            duration: 1000,
            easing: 'swing',
            step: function(now) {
                $(this).text(Math.ceil(now));
            }
        });
    });

}); // End of use strict

// easypie chart
$(function() {
    'use strict'
    $('.easypie').easyPieChart({
        easing: 'easeOutBounce',
        onStep: function(from, to, percent) {
            $(this.el).find('.percent').text(Math.round(percent));
        }
    });
    var chart = window.chart = $('.easypie').data('easyPieChart');
    $('.js_update').on('click', function() {
        chart.update(Math.random() * 200 - 100);
    });
}); // End of use strict

// ------------------------------