$(function() {
	
	
		/* Apexcharts (#bar) */
		window.Apex = {
			dataLabels: {
				enabled: false
			}
		};

		
		var optionsBar = {
		chart: {
			type: 'bar',
			height: 249,
			stacked:'true',
			width: '100%',
			foreColor: '#999'
		},
		plotOptions: {
			bar: {
			  dataLabels: {
				enabled: false
			  },
			  columnWidth: '33%',
			  endingShape: 'rounded'
			}
		},
		colors: ["#285cf7", '#00cccc'],
		series: [{
			name: "Sessions",
			data: [20, 16, 24, 28, 26, 22, 15, 5, 14, 16, 22, 29, 24, 19, 15, 10, 11, 15, 19, 23],
			}, {
				name: "Views",
				data: [20, 16, 24, 28, 26, 22, 15, 5, 14, 16, 22, 29, 24, 19, 15, 10, 11, 15, 19, 23],
			}],
		labels: [15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 1, 2, 3, 4],
		xaxis: {
		axisBorder: {
			show: false
		},
		axisTicks: {
			show: false
		},
		crosshairs: {
			show: false
		},
		labels: {
			show: false,
			style: {
				fontSize: '14px'
			}
			},
	  },
	  grid: {
		xaxis: {
		  lines: {
			show: false
		  },
		},
		yaxis: {
		  lines: {
			show: false
		  },
		}
	  },
	  yaxis: {
		axisBorder: {
		  show: false
		},
		labels: {
		  show: false
		},
	  },
	  
	  legend: {
		  show: false,
		floating: true,
		position: 'top',
		horizontalAlign: 'right',
		offsetY: 0
	  },
	 
	 
	  tooltip: {
		shared: true
	  }

	}

	var chartBar = new ApexCharts(document.querySelector('#bar'), optionsBar);
	chartBar.render();
	
	/* Apexcharts (#bar) closed */ 
	
	
	/* Flotchart */ 
	 $.plot('#flotChart5', [{
            data: dashData2,
            color: '#00cccc'
          },{
            data: dashData3,
            color: '#007bff'
          },{
            data: dashData4,
            color: '#f10075'
          }], {
    			series: {
    				shadowSize: 0,
            lines: {
              show: true,
              lineWidth: 2,
              fill: false,
              fillColor: { colors: [ { opacity: 0 }, { opacity: 1 } ] }
            }
    			},
          grid: {
            borderWidth: 0,
            labelMargin: 20
          },
    			yaxis: {
            show: false,
            min: 0,
            max: 100
          },
    			xaxis: {
            show: true,
            color: 'rgba(239, 242, 246, 0.5)',
            ticks: [
              [0, ''],
              [10, '<span>Nov</span><span>05</span>'],
              [20, '<span>Nov</span><span>10</span>'],
              [30, '<span>Nov</span><span>15</span>'],
              [40, '<span>Nov</span><span>18</span>'],
              [50, '<span>Nov</span><span>22</span>'],
              [60, '<span>Nov</span><span>26</span>'],
              [70, '<span>Nov</span><span>30</span>'],
            ]
          }
    });
	/* Flotchart closed */ 
	
	
	/* Chartjs (#bar-chart-horizontal) */
	new Chart(document.getElementById("bar-chart-horizontal"), {
    type: 'horizontalBar',
	data: {
		labels: ["Organic", "Direct", "Campagion", "Referral" ],
		datasets: [
				{
					label: "Traffic Source",
					backgroundColor: ["#285cf7", "#00cccc","#f10075","#ffc107"],
					data: [5478,4767,3934, 2945],
				}
			]
		},
		options: {
			responsive: true,
			maintainAspectRatio: false,
			tooltips: {
				mode: 'index',
				titleFontSize: 12,
				titleFontColor: '#000',
				bodyFontColor: '#000',
				backgroundColor: '#fff',
				cornerRadius: 3,
				intersect: false,

			},
			legend: {
				display: false,
				labels: {
					usePointStyle: true,
				},
			},
			scales: {
				xAxes: [{
					 barPercentage: 0.1,
					 barSpacing:5,
					ticks: {
						fontColor: "#8e9cad",
					 },
					display: true,
					gridLines: {
						display: true,
						color: 'rgba(142, 156, 173,0.1)',
						drawBorder: false
					},
					scaleLabel: {
						display: false,
						labelString: 'Month',
						fontColor: '#8492a6 '
					}
				}],
				yAxes: [{
					 barPercentage: 0.8,
					 barSpacing:1,
					ticks: {
						fontColor: "#8e9cad",
					 },
					display: true,
					gridLines: {
						display: true,
						color: 'rgba(142, 156, 173,0.1)',
						drawBorder: false
					},
					scaleLabel: {
						display: false,
						labelString: 'sales',
						fontColor: '#8492a6 '
					}
				}]
			},
			title: {
				display: false,
				text: 'Normal Legend'
			}
		}
	});
	/* Chartjs (#bar-chart-horizontal) closed */
	
	
	/* Chartjs (#flotPie) */
	$.plot('#flotPie', [{
 		label: 'Very Satisfied',
 		data: [
 			[1, 25]
 		],
 		color: '#6f42c1'
 	}, {
 		label: 'Satisfied',
 		data: [
 			[1, 38]
 		],
 		color: '#007bff'
 	}, {
 		label: 'Not Satisfied',
 		data: [
 			[1, 20]
 		],
 		color: '#00cccc'
 	}, {
 		label: 'Very Unsatisfied',
 		data: [
 			[1, 15]
 		],
 		color: '#f10075'
 	}], {
 		series: {
 			pie: {
 				show: true,
 				radius: 1,
 				innerRadius: 0.5,
 				label: {
 					show: true,
 					radius: 3 / 4,
 					formatter: labelFormatter
 				}
 			}
 		},
 		legend: {
 			show: false
 		}
 	});
	
	function labelFormatter(label, series) {
 		return '<div style="font-size:11px; font-weight:500; text-align:center; padding:2px; color:white;">' + Math.round(series.percent) + '%<\/div>';
 	}
	/* Chartjs (#flotPie) closed */
	
	
	// P-scroll
	var ps4 = new PerfectScrollbar('.rating-scroll', {
	  useBothWheelAxes:true,
	  suppressScrollX:true,
	});
	
	/* Piety */
	if($('.peity-donut').length) {
		$('.peity-donut').peity('donut');
	  }

	if($('.peity-bar').length) {
		$('.peity-bar').peity('bar');
	 }
	
	
});

	
