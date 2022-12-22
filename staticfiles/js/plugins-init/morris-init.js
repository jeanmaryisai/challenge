(function($) {
    "use strict"

    var dlabMorris = function() {

        var screenWidth = $(window).width();

        var setChartWidth = function() {
            if (screenWidth <= 768) {
                var chartBlockWidth = 0;
                chartBlockWidth = (screenWidth < 300) ? screenWidth : 300;
                jQuery('.morris_chart_height').css('min-width', chartBlockWidth - 31);
            }
        }

        var donutChart = function() {
            Morris.Donut({
                element: 'morris_donught',
                data: [{
                    label: "\xa0 \xa0 Download Sales \xa0 \xa0",
                    value: 12,

                }, {
                    label: "\xa0 \xa0 In-Store Sales \xa0 \xa0",
                    value: 30
                }, {
                    label: "\xa0 \xa0 Mail-Order Sales \xa0 \xa0",
                    value: 20
                }],
                resize: true,
                redraw: true,
                colors: ['#5bcfc5', 'rgb(255, 92, 0)', '#709fba'],
                //responsive:true,

            });
        }

        var lineChart = function() {
            //line chart
            const logs = document.getElementById('logs').children
            var dataa = []

            console.log(logs[0])
            for (let x = 0; x < logs.length; x++) {
                const element = logs[x]
                var a = element.dataset['numero']
                var b = element.dataset['manche']
                var c = element.dataset['points']
                let d = (x + 1) + " Qst" + a
                console.log(b)
                dataa.push({ y: d, Manche: parseInt(b), item1: parseInt(c) })
            }

            let line = new Morris.Line({
                element: 'morris_line',
                resize: true,
                data: dataa,
                // data: [{
                // 		y: '1 Qst23',
                // 		Manche: 1,
                // 		item1: 50
                // 	},
                // 	{
                // 		y: '2 Qst23',
                // 		item1: 20,
                // 		Manche: 1,
                // 	},
                // 	{
                // 		y: '3 Qst05',
                // 		item1: 30,
                // 		Manche: 1,
                // 	},
                // 	{
                // 		y: '4 Qst00',
                // 		item1: 10,
                // 		Manche: 2,
                // 	},
                // 	{
                // 		y: '5 Qst34',
                // 		item1: 12,
                // 		Manche: 2,
                // 	},
                // 	{
                // 		y: '6 Qst65',
                // 		item1: 32,
                // 		Manche: 2,
                // 	},
                // 	{
                // 		y: '7 Qst75',
                // 		item1: 42,
                // 		Manche: 3,
                // 	},
                // 	{
                // 		y: '8 Qst54',
                // 		item1: 50,
                // 		Manche: 3,
                // 	},
                // 	{
                // 		y: '9 Qst63',
                // 		item1: 34,
                // 		Manche: 3,
                // 	},
                // 	{
                // 		y: '10 Qst76',
                // 		item1: 43,
                // 		Manche: 4,
                // 	},
                // 	{
                // 		y: '11 Qst73',
                // 		item1: 25,
                // 		Manche: 4,
                // 	},
                // 	{
                // 		y: '12 Qst43',
                // 		item1: 10,
                // 		Manche: 4,
                // 	},
                // 	{
                // 		y: '13 Qst13',
                // 		item1: 30,
                // 		Manche: 5,
                // 	},
                // 	{
                // 		y: '14 Qst03',
                // 		item1: 24,
                // 		Manche: 5,
                // 	},
                // 	{
                // 		y: '15 Qst24',
                // 		item1: 32,
                // 		Manche: 5,
                // 	}
                // ],
                xkey: 'y',
                ykeys: ['item1', 'Manche'],
                labels: ['Points cummulee', 'Manche'],
                gridLineColor: 'transparent',
                lineColors: ['rgb(238, 60, 60)', 'rgba(0,0,0,0)'], //here
                lineWidth: 1,
                hideHover: 'auto',
                pointSize: 0,
                axes: false
            });
        }

        var lineChart2 = function() {
            //Area chart
            Morris.Area({
                element: 'line_chart_2',
                data: [{
                        period: '2001',
                        smartphone: 0,
                        windows: 0,
                        mac: 0
                    }, {
                        period: '2002',
                        smartphone: 90,
                        windows: 60,
                        mac: 25
                    }, {
                        period: '2003',
                        smartphone: 40,
                        windows: 80,
                        mac: 35
                    }, {
                        period: '2004',
                        smartphone: 30,
                        windows: 47,
                        mac: 17
                    }, {
                        period: '2005',
                        smartphone: 150,
                        windows: 40,
                        mac: 120
                    }, {
                        period: '2006',
                        smartphone: 25,
                        windows: 80,
                        mac: 40
                    }, {
                        period: '2007',
                        smartphone: 10,
                        windows: 10,
                        mac: 10
                    }


                ],
                xkey: 'period',
                ykeys: ['smartphone', 'windows', 'mac'],
                labels: ['Phone', 'Windows', 'Mac'],
                pointSize: 3,
                fillOpacity: 0,
                pointStrokeColors: ['#EE3C3C', '#709fba', '#5bcfc5'],
                behaveLikeLine: true,
                gridLineColor: 'transparent',
                lineWidth: 3,
                hideHover: 'auto',
                lineColors: ['rgb(238, 60, 60)', 'rgb(0, 171, 197)', '#5bcfc5'],
                resize: true

            });
        }

        var barChart = function() {
            if (jQuery('#morris_bar').length > 0) {
                //bar chart
                Morris.Bar({
                    element: 'morris_bar',
                    data: [{
                        y: '2006',
                        a: 100,
                        b: 90,
                        c: 60
                    }, {
                        y: '2007',
                        a: 75,
                        b: 65,
                        c: 40
                    }, {
                        y: '2008',
                        a: 50,
                        b: 40,
                        c: 30
                    }, {
                        y: '2009',
                        a: 75,
                        b: 65,
                        c: 40
                    }, {
                        y: '2010',
                        a: 50,
                        b: 40,
                        c: 30
                    }, {
                        y: '2011',
                        a: 75,
                        b: 65,
                        c: 40
                    }, {
                        y: '2012',
                        a: 100,
                        b: 90,
                        c: 40
                    }],
                    xkey: 'y',
                    ykeys: ['a', 'b', 'c'],
                    labels: ['A', 'B', 'C'],
                    barColors: ['#5bcfc5', '#709fba', '#ff9f00'],
                    hideHover: 'auto',
                    gridLineColor: 'transparent',
                    resize: true,
                    barSizeRatio: 0.25,
                });
            }
        }

        var barStalkChart = function() {
            //bar chart
            Morris.Bar({
                element: 'morris_bar_stalked',
                data: [{
                    y: 'S',
                    a: 66,
                    b: 34
                }, {
                    y: 'M',
                    a: 75,
                    b: 25
                }, {
                    y: 'T',
                    a: 50,
                    b: 50
                }, {
                    y: 'W',
                    a: 75,
                    b: 25
                }, {
                    y: 'T',
                    a: 50,
                    b: 50
                }, {
                    y: 'F',
                    a: 16,
                    b: 84
                }, {
                    y: 'S',
                    a: 70,
                    b: 30
                }, {
                    y: 'S',
                    a: 30,
                    b: 70
                }, {
                    y: 'M',
                    a: 40,
                    b: 60
                }, {
                    y: 'T',
                    a: 29,
                    b: 71
                }, {
                    y: 'W',
                    a: 44,
                    b: 56
                }, {
                    y: 'T',
                    a: 30,
                    b: 70
                }, {
                    y: 'F',
                    a: 60,
                    b: 40
                }, {
                    y: 'G',
                    a: 40,
                    b: 60
                }, {
                    y: 'S',
                    a: 46,
                    b: 54
                }],
                xkey: 'y',
                ykeys: ['a', 'b'],
                labels: ['A', 'B'],
                barColors: ['#5bcfc5', "#F1F3F7"],
                hideHover: 'auto',
                gridLineColor: 'transparent',
                resize: true,
                barSizeRatio: 0.25,
                stacked: true,
                behaveLikeLine: true,
                //redraw: true

                // barRadius: [6, 6, 0, 0]
            });

        }

        var areaChart = function() {
            //area chart
            Morris.Area({
                element: 'morris_area',
                data: [{
                        period: '2001',
                        smartphone: 0,
                        windows: 0,
                        mac: 0
                    }, {
                        period: '2002',
                        smartphone: 90,
                        windows: 60,
                        mac: 25
                    }, {
                        period: '2003',
                        smartphone: 40,
                        windows: 80,
                        mac: 35
                    }, {
                        period: '2004',
                        smartphone: 30,
                        windows: 47,
                        mac: 17
                    }, {
                        period: '2005',
                        smartphone: 150,
                        windows: 40,
                        mac: 120
                    }, {
                        period: '2006',
                        smartphone: 25,
                        windows: 80,
                        mac: 40
                    }, {
                        period: '2007',
                        smartphone: 10,
                        windows: 10,
                        mac: 10
                    }


                ],
                lineColors: ['#5bcfc5', 'rgb(16, 202, 147)', 'rgb(255, 92, 0)'],
                xkey: 'period',
                ykeys: ['smartphone', 'windows', 'mac'],
                labels: ['Phone', 'Windows', 'Mac'],
                pointSize: 0,
                lineWidth: 0,
                resize: true,
                fillOpacity: 0.95,
                behaveLikeLine: true,
                gridLineColor: 'transparent',
                hideHover: 'auto'

            });
        }

        var areaChart2 = function() {
            if (jQuery('#morris_area_2').length > 0) {
                //area chart
                Morris.Area({
                    element: 'morris_area_2',
                    data: [{
                            period: '2010',
                            SiteA: 0,
                            SiteB: 0,

                        }, {
                            period: '2011',
                            SiteA: 130,
                            SiteB: 100,

                        }, {
                            period: '2012',
                            SiteA: 80,
                            SiteB: 60,

                        }, {
                            period: '2013',
                            SiteA: 70,
                            SiteB: 200,

                        }, {
                            period: '2014',
                            SiteA: 180,
                            SiteB: 150,

                        }, {
                            period: '2015',
                            SiteA: 105,
                            SiteB: 90,

                        },
                        {
                            period: '2016',
                            SiteA: 250,
                            SiteB: 150,

                        }
                    ],
                    xkey: 'period',
                    ykeys: ['SiteA', 'SiteB'],
                    labels: ['Site A', 'Site B'],
                    pointSize: 0,
                    fillOpacity: 0.6,
                    pointStrokeColors: ['#b4becb', '#00A2FF'], //here
                    behaveLikeLine: true,
                    gridLineColor: 'transparent',
                    lineWidth: 0,
                    smooth: false,
                    hideHover: 'auto',
                    lineColors: ['rgb(0, 171, 197)', 'rgb(0, 0, 128)'],
                    resize: true

                });
            }
        }


        /* Function ============ */
        return {
            init: function() {
                setChartWidth();
                // donutChart();
                lineChart();
                lineChart2();
                barChart();
                barStalkChart();
                areaChart();
                areaChart2();
            },


            resize: function() {
                screenWidth = $(window).width();
                setChartWidth();
                // donutChart();
                lineChart();
                // lineChart2();
                // barChart();
                // barStalkChart();
                // areaChart();
                // areaChart2();
            }
        }

    }();

    jQuery(document).ready(function() {
        dlabMorris.init();
        //dlabMorris.resize();

    });

    jQuery(window).on('load', function() {
        //dlabMorris.init();
    });

    jQuery(window).resize(function() {
        //dlabMorris.resize();
        //dlabMorris.init();
    });

})(jQuery);