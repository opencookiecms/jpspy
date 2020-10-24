var color = Chart.helpers.color;
	function createConfig(legendPosition, colorName) {
		return {
			type: 'line',
			data: {
				labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
				datasets: [{
					label: 'My First dataset',
					data: [
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor(),
						randomScalingFactor()
					],
					backgroundColor: color(window.chartColors[colorName]).alpha(0).rgbString(),
					borderColor: window.chartColors[colorName],
					borderWidth: 5
				}]
			},
			
			options: {
				responsive: true,
				legend: {
					position: legendPosition,
					display: false,
				},
				
				scales: {
					xAxes: [{
						display: true,
						scaleLabel: {
							display: false,
							labelString: 'Week'
						}
					}],
					yAxes: [{
						display: true,
						scaleLabel: {
							display: true,
							labelString: 'Value'
						}
					}]
				},
				
			}
		};
	}

	window.onload = function() {
		[{
			id: 'chart-legend-top',
			legendPosition: 'top',
			color: 'purple'
		}, {
			id: 'chart-legend-right',
			legendPosition: 'right',
			color: 'blue'
		}, {
			id: 'chart-legend-bottom',
			legendPosition: 'bottom',
			color: 'green'
		}, {
			id: 'chart-legend-left',
			legendPosition: 'left',
			color: 'red'
		}].forEach(function(details) {
			var ctx = document.getElementById(details.id).getContext('2d');
			var config = createConfig(details.legendPosition, details.color);
			new Chart(ctx, config);
			ctx.shadowBlur = 10;
			ctx.shadowOffsetX = 1;
			ctx.shadowOffsetY = 1;
		});
	};