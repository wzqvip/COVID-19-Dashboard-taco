  function myFunction() {
      var x,xyqz,xyys,xyzz,ljqz,zy,sw;
      var jishu=0;
      var myDate=new Array("1月24日","1月25日","1月26日","1月27日","1月28日","1月29日","1月30日","1月31日","2月1日","2月2日","2月3日","2月4日","2月5日","2月6日","2月7日","2月8日","2月9日","2月10日","2月11日","2月12日","2月13日","2月14日","2月15日",
        "2月16日","2月17日","2月18日","2月19日","2月20日","2月21日","2月22日","2月23日","2月24日","2月25日","2月26日","2月27日","2月28日",);
      var xyqzs=new Array(1208,1870,2613,4349,5739,7417,9308,11289,13748,16369,19381,22942,26302,28985,31774,33738,35982,37626,38800,52526,55748,56873,57416,
                          57934,58016,57805,56303,54965,53284,51606,49824,47672,45604,43258,39919,37414);
      var xyyss=new Array(1965,2684,5794,6973,9239,12167,15238,17988,19544,21558,23214,23260,24702,26359,27657,28942,23589,21675,16067,13435,10109,8969,8228,
                          7264,6242,5248,4922,5206,5365,4148,3434,2824,2491,2358,2308,1418);
      var xyzzs=new Array(237,324,416,976,1239,1370,1527,1795,2110,2296,2788,3219,3859,4821,6101,6188,6484,7333,8204,8030,10204,11053,11272,10644,11741,11977,
                          11864,11633,11477,10968,9915,9126,8752,8346,7952,7664);
      var ljqzs=new Array(1287,1975,2744,4515,5974,7711,9692,11791,14380,17205,20438,24324,28018,31161,34546,37198,40171,42653,44653,59804,63851,66492,68500,70548,
                          72436,74185,74576,75465,76288,76936,77150,77658,78064,78497,78824,79251);
      var zys=new Array(38,49,51,60,103,124,171,243,328,475,632,892,1153,1540,2050,2649,3281,3996,4740,5911,6723,8096,9419,10844,12552,14376,16155,18264,20659,
                        22888,24734,27323,29745,32495,36117,39002);
      var sws=new Array(41,56,80,106,132,170,213,259,304,361,425,490,563,636,722,811,908,116,1113,1367,1380,1523,1165,1770,1868,2004,2118,2236,2345,2442,2592,
                        2663,2715,2744,2788,2835);
    x = document.getElementById("inputdate").value;
   for(var i=0;i<myDate.length;i++){
    if(x==myDate[i]){
      jishu++;
      xyqz=xyqzs[i];
      xyys=xyyss[i];
      xyzz=xyzzs[i];
      ljqz=ljqzs[i];
      sw=sws[i];
      zy=zys[i];
    document.getElementById("现有确诊病例").innerHTML = xyqz;
    document.getElementById("现有疑似病例").innerHTML = xyys;
    document.getElementById("现有重症病例").innerHTML = xyzz;
    document.getElementById("累计确诊病例").innerHTML = ljqz;
    document.getElementById("治愈病例").innerHTML = zy;
    document.getElementById("死亡病例").innerHTML = sw;
    

    }
   }
   if(jishu==0){
    alert("输入内容不符合要求");
   }  
}