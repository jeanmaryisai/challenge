(function($) {
    /* "use strict" */

    var dlabChartlist = function() {

        var screenWidth = $(window).width();

        var pieChart = function() {
            if (jQuery('#pieChart').length > 0) {
                //doughut chart
                const pieChart = document.getElementById("pieChart").getContext('2d');
                // pieChart.height = 100;
                new Chart(pieChart, {
                    type: 'doughnut',
                    data: {
                        labels: [
                            'repondus',
                            'repliques',
                            'ratee'
                        ],
                        weight: 5,
                        defaultFontFamily: 'Poppins',
                        datasets: [{
                            data: [parseInt(document.getElementById('home_questions_ans_total').dataset['percent']),
                                parseInt(document.getElementById('home_questions_replique_total').dataset['percent']),
                                parseInt(document.getElementById('home_questions_missed_total').dataset['percent']),
                            ],
                            borderWidth: 0,
                            borderColor: "rgba(255,255,255,1)",
                            backgroundColor: [
                                "#8df05f",
                                "#ff4b4b",
                                "#e3e3e3"
                            ],
                            hoverBackgroundColor: [
                                "#8df05f",
                                "#ff4b4b",
                                "#e3e3e3"
                            ],

                            hoverOffset: 4

                        }],
                    },
                    options: {
                        weight: 1,
                        cutoutPercentage: 70,
                        responsive: true,
                        maintainAspectRatio: false
                    }
                });
            }
        }




        var lineChart = function() {
            const donnees = document.getElementById('donnees').children
            var data = []
            for (let index = 0; index < donnees.length; index++) {
                const l = donnees[index];
                data.push({
                    name: l.dataset['prenom'],
                    data: [
                        parseInt(l.dataset[1]),
                        parseInt(l.dataset[2]),
                        parseInt(l.dataset[3]),
                        parseInt(l.dataset[4]),
                        parseInt(l.dataset[5]),
                    ]
                })
            }
            var options = {
                series: data,
                // series: [{
                //         name: "Youselyne",
                //         data: [10, 30, 20, 40, 20, 0]
                //     },
                //     {
                //         name: "Dave",
                //         data: [10, 25, 0, 35, 35, 0]
                //     },
                //     {
                //         name: "Sterline",
                //         data: [10, 15, 10, 30, 15, 0]
                //     },
                //     {
                //         name: "Rose Berlie",
                //         data: [20, 10, 12, 0, 02, 0]
                //     },
                //     {
                //         name: "Snayder",
                //         data: [55, 45, 25, 25, 50, 0]
                //     }
                // ],
                chart: {
                    height: 170,
                    type: 'line',
                    toolbar: {
                        show: false
                    },
                    zoom: {
                        enabled: false
                    }
                },
                colors: ['#68e365', '#ff4b4b', '#969ba0', '#498c80', '#384900', '#fff321'],
                dataLabels: {
                    enabled: false
                },
                stroke: {
                    curve: 'smooth',
                    width: 3
                },
                legend: {
                    show: false
                },
                grid: {
                    /* row: {
			colors: ['#f3f3f3', 'transparent'], // takes an array which will be repeated on columns
			opacity: 0.5
		  }, */
                    xaxis: {
                        lines: {
                            show: true
                        }
                    },
                },
                xaxis: {
                    categories: ['1ere', '2eme', '3eme', '4eme', '5eme'],
                },
                yaxis: {
                    show: false
                }
            };

            var chart = new ApexCharts(document.querySelector("#line-chart"), options);
            chart.render();
        }

        /* Function ============ */
        return {
            init: function() {},


            load: function() {

                pieChart();
                lineChart();
            },

            resize: function() {}
        }

    }();



    jQuery(window).on('load', function() {
        setTimeout(function() {
            dlabChartlist.load();
        }, 1000);

    });



})(jQuery);