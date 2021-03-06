 var myChart = echarts.init(document.getElementById('chart'));
  
        var option = {
            title:{
                text:'广东疫情数据统计'
            },
            legend: {
                orient:'horizontal',
                x:'right',
                y:'35px',
                padding:0
            },
            
            tooltip: {
                 trigger: 'axis', 
                 axisPointer: {  
                 type: 'line', 
                 crossStyle: {
                 color: '#fff'
                 }  
                 }

            },
            dataset: {
                
                source: [
                    ['日期','现有确诊病例','累计确诊病例','死亡病例','治愈病例'],
                    ['1月24日',76,78,0,2],
                    ['1月25日',109,111,0,2],
                    ['1月26日',144,146,0,2],
                    ['1月27日',184,188,0,4],
                    ['1月28日',236,241,0,5],
                    ['1月29日',305,311,0,6],
                    ['1月30日',386,393,0,7],
                    ['1月31日',512,520,0,8],
                    ['2月1日',592,604,0,12],
                    ['2月2日',669,683,0,14],
                    ['2月3日',777,797,0,20],
                    ['2月4日',838,870,0,32],
                    ['2月5日',895,944,0,49],
                    ['2月6日',949,1018,1,68],
                    ['2月7日',977,1075,1,97],
                    ['2月8日',994,1120,1,125],
                    ['2月9日',1007,1151,1,143],
                    ['2月10日',995,1177,1,181],
                    ['2月11日',977,1219,1,241],
                    ['2月12日',955,1241,2,284],
                    ['2月13日',927,1261,2,332],
                    ['2月14日',906,1294,2,386],
                    ['2月15日',878,1316,2,436],
                    ['2月16日',845,1322,4,473],
                    ['2月17日',794,1328,4,530],
                    ['2月18日',755,1331,5,571],
                    ['2月19日',708,1332,5,619],
                    ['2月20日',664,1333,5,664],
                    ['2月21日',614,1339,5,720],
                    ['2月22日',596,1342,6,740],
                    ['2月23日',567,1345,6,772],
                    ['2月24日',535,1347,7,805],
                    ['2月25日',499,1347,7,841],
                    ['2月26日',487,1347,7,873],
                    
                ]
            },
            
            xAxis: {type: 'category',
                name:'日期',
                axisLabel:{
                    rotate:-45,
                    interval:1
                }, 
                splitArea : {
                show: true,
                areaStyle:{
                    color:['rgba(144,238,144,0.3)','rgba(135,200,250,0.3)']
                }
                }
             },
           
            yAxis: {
                
            },
    
            series: [
                {type: 'line'},
                {type: 'line'},
                {type: 'line'},
                {type: 'line'}
            
            ]
        };
 
    
        myChart.setOption(option);