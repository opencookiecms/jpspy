 $(function() {
 	'use strict'
 	$.plot('#flotChart', [{
 		data: dashData1,
 		color: '#3d0894',
 		bars: {
 			show: true,
 			lineWidth: 0,
 			barWidth: .5,
 			fill: 1
 		}
 	}, {
 		data: dashData4,
 		color: '#2d066d',
 		bars: {
 			show: true,
 			lineWidth: 0,
 			barWidth: .5,
 			fill: 1
 		}
 	}], {
 		series: {
 			shadowSize: 0
 		},
 		grid: {
 			borderWidth: 0,
 			labelMargin: 10
 		},
 		yaxis: {
 			show: true,
 			min: 0,
 			max: 45,
 			ticks: 4,
 			tickColor: 'rgba(255,255,255,.08)',
 			font: {
 				color: 'rgba(255,255,255,0)'
 			}
 		},
 		xaxis: {
 			show: true,
 			position: 'top',
 			tickColor: 'rgba(255,255,255,.08)',
 			font: {
 				color: 'rgba(255,255,255,.2)',
 				size: 11
 			}
 		}
 	});
 	// animated smooth scroll on target from top menu
 	$('#mainDemoBtn').on('click', function(e) {
 		var target = $(this).attr('href');
 		$('html, body').animate({
 			scrollTop: $('' + target).offset().top
 		}, 500);
 		e.preventDefault();
 	});
 })