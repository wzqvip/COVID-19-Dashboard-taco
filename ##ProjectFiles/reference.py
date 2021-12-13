# import json
# import requests

# url = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist'
# response = requests.post(url).text


# resp = json.loads(response)   #使用变量resp来接收字典格式的数据
# for data in resp['data']:  #遍历提取每个国家的疫情数据
#     name = data['name']   #国家名
#     confirm = data['confirm']   #该国家疫情人数
#     print(name,confirm)

# map_version = {}  #定义空字典
# for data in resp['data']:  #遍历提取每个国家的疫情数据
#     name = data['name']   #国家名
#     confirm = data['confirm']   #该国家疫情人数
#     map_version[name] = int(confirm)  #将国家和人数以键值对的形式传入字典

# element = list(map_version.items())

# from pyecharts.charts import Map,Geo

# map = Map().add(series_name="世界疫情分布图",  #名称
#                 data_pair=element,   #传入数据
#                 maptype='world',   #地图类型
#                 )
# map.render('map.html')  #命名并保存

# from pyecharts import options
# #设置可视化地图
# map.set_series_opts(label_opts=options.LabelOpts(is_show=False))  #不显示国家名

# #按照感染人数的不同，给地图添加不同的颜色
# #设置全局配置项
# map.set_global_opts(visualmap_opts=options.VisualMapOpts(max_=1100000,is_piecewise=True,pieces=[
#                  {"min": 500000},
#                  {"min": 200000, "max": 499999},
#                  {"min": 100000, "max": 199999},
#                  {"min": 50000, "max": 99999},
#                  {"min": 10000, "max": 49999},
#                  {"max": 9999},]))

# #代表国家首都的圆点不美观，去掉红点：
# map = Map().add(
#                                     is_map_symbol_show=False,  #不显示标记
#                                     ）

# #设置背景ma颜色并为网页取名：
# map = Map(options.InitOpts(bg_color="#87CEFA",page_title='世界疫情分布')).add()



# import requests
# import json
# from pyecharts.charts import Map
# from pyecharts import options

# url = 'https://api.inews.qq.com/newsqa/v1/automation/foreign/country/ranklist'
# response = requests.post(url).text
# resp = json.loads(response)   #使用变量resp来接收字典格式的数据
# map_version = {}  #定义空字典
# for data in resp['data']:  #遍历提取每个国家的疫情数据
#     name = data['name']   #国家名
#     confirm = data['confirm']   #该国家疫情人数
#     map_version[name] = int(confirm)  #将国家和人数以键值对的形式传入字典
# element = list(map_version.items())   #将字典值调整为可以传入地图的格式
# name_map = {
#     'Singapore Rep.': '新加坡',
#     'Dominican Rep.': '多米尼加',
#     'Palestine': '巴勒斯坦',
#     'Bahamas': '巴哈马',
#     'Timor-Leste': '东帝汶',
#     'Afghanistan': '阿富汗',
#     'Guinea-Bissau': '几内亚比绍',
#     "Côte d'Ivoire": '科特迪瓦',
#     'Siachen Glacier': '锡亚琴冰川',
#     "Br. Indian Ocean Ter.": '英属印度洋领土',
#     'Angola': '安哥拉',
#     'Albania': '阿尔巴尼亚',
#     'United Arab Emirates': '阿联酋',
#     'Argentina': '阿根廷',
#     'Armenia': '亚美尼亚',
#     'French Southern and Antarctic Lands': '法属南半球和南极领地',
#     'Australia': '澳大利亚',
#     'Austria': '奥地利',
#     'Azerbaijan': '阿塞拜疆',
#     'Burundi': '布隆迪',
#     'Belgium': '比利时',
#     'Benin': '贝宁',
#     'Burkina Faso': '布基纳法索',
#     'Bangladesh': '孟加拉国',
#     'Bulgaria': '保加利亚',
#     'The Bahamas': '巴哈马',
#     'Bosnia and Herz.': '波斯尼亚和黑塞哥维那',
#     'Belarus': '白俄罗斯',
#     'Belize': '伯利兹',
#     'Bermuda': '百慕大',
#     'Bolivia': '玻利维亚',
#     'Brazil': '巴西',
#     'Brunei': '文莱',
#     'Bhutan': '不丹',
#     'Botswana': '博茨瓦纳',
#     'Central African Rep.': '中非',
#     'Canada': '加拿大',
#     'Switzerland': '瑞士',
#     'Chile': '智利',
#     'China': '中国',
#     'Ivory Coast': '象牙海岸',
#     'Cameroon': '喀麦隆',
#     'Dem. Rep. Congo': '刚果民主共和国',
#     'Congo': '刚果',
#     'Colombia': '哥伦比亚',
#     'Costa Rica': '哥斯达黎加',
#     'Cuba': '古巴',
#     'N. Cyprus': '北塞浦路斯',
#     'Cyprus': '塞浦路斯',
#     'Czech Rep.': '捷克',
#     'Germany': '德国',
#     'Djibouti': '吉布提',
#     'Denmark': '丹麦',
#     'Algeria': '阿尔及利亚',
#     'Ecuador': '厄瓜多尔',
#     'Egypt': '埃及',
#     'Eritrea': '厄立特里亚',
#     'Spain': '西班牙',
#     'Estonia': '爱沙尼亚',
#     'Ethiopia': '埃塞俄比亚',
#     'Finland': '芬兰',
#     'Fiji': '斐',
#     'Falkland Islands': '福克兰群岛',
#     'France': '法国',
#     'Gabon': '加蓬',
#     'United Kingdom': '英国',
#     'Georgia': '格鲁吉亚',
#     'Ghana': '加纳',
#     'Guinea': '几内亚',
#     'Gambia': '冈比亚',
#     'Guinea Bissau': '几内亚比绍',
#     'Eq. Guinea': '赤道几内亚',
#     'Greece': '希腊',
#     'Greenland': '格陵兰',
#     'Guatemala': '危地马拉',
#     'French Guiana': '法属圭亚那',
#     'Guyana': '圭亚那',
#     'Honduras': '洪都拉斯',
#     'Croatia': '克罗地亚',
#     'Haiti': '海地',
#     'Hungary': '匈牙利',
#     'Indonesia': '印度尼西亚',
#     'India': '印度',
#     'Ireland': '爱尔兰',
#     'Iran': '伊朗',
#     'Iraq': '伊拉克',
#     'Iceland': '冰岛',
#     'Israel': '以色列',
#     'Italy': '意大利',
#     'Jamaica': '牙买加',
#     'Jordan': '约旦',
#     'Japan': '日本',
#     'Kazakhstan': '哈萨克斯坦',
#     'Kenya': '肯尼亚',
#     'Kyrgyzstan': '吉尔吉斯斯坦',
#     'Cambodia': '柬埔寨',
#     'Korea': '韩国',
#     'Kosovo': '科索沃',
#     'Kuwait': '科威特',
#     'Lao PDR': '老挝',
#     'Lebanon': '黎巴嫩',
#     'Liberia': '利比里亚',
#     'Libya': '利比亚',
#     'Sri Lanka': '斯里兰卡',
#     'Lesotho': '莱索托',
#     'Lithuania': '立陶宛',
#     'Luxembourg': '卢森堡',
#     'Latvia': '拉脱维亚',
#     'Morocco': '摩洛哥',
#     'Moldova': '摩尔多瓦',
#     'Madagascar': '马达加斯加',
#     'Mexico': '墨西哥',
#     'Macedonia': '马其顿',
#     'Mali': '马里',
#     'Myanmar': '缅甸',
#     'Montenegro': '黑山',
#     'Mongolia': '蒙古',
#     'Mozambique': '莫桑比克',
#     'Mauritania': '毛里塔尼亚',
#     'Malawi': '马拉维',
#     'Malaysia': '马来西亚',
#     'Namibia': '纳米比亚',
#     'New Caledonia': '新喀里多尼亚',
#     'Niger': '尼日尔',
#     'Nigeria': '尼日利亚',
#     'Nicaragua': '尼加拉瓜',
#     'Netherlands': '荷兰',
#     'Norway': '挪威',
#     'Nepal': '尼泊尔',
#     'New Zealand': '新西兰',
#     'Oman': '阿曼',
#     'Pakistan': '巴基斯坦',
#     'Panama': '巴拿马',
#     'Peru': '秘鲁',
#     'Philippines': '菲律宾',
#     'Papua New Guinea': '巴布亚新几内亚',
#     'Poland': '波兰',
#     'Puerto Rico': '波多黎各',
#     'Dem. Rep. Korea': '朝鲜',
#     'Portugal': '葡萄牙',
#     'Paraguay': '巴拉圭',
#     'Qatar': '卡塔尔',
#     'Romania': '罗马尼亚',
#     'Russia': '俄罗斯',
#     'Rwanda': '卢旺达',
#     'W. Sahara': '西撒哈拉',
#     'Saudi Arabia': '沙特阿拉伯',
#     'Sudan': '苏丹',
#     'S. Sudan': '南苏丹',
#     'Senegal': '塞内加尔',
#     'Solomon Is.': '所罗门群岛',
#     'Sierra Leone': '塞拉利昂',
#     'El Salvador': '萨尔瓦多',
#     'Somaliland': '索马里兰',
#     'Somalia': '索马里',
#     'Serbia': '塞尔维亚',
#     'Suriname': '苏里南',
#     'Slovakia': '斯洛伐克',
#     'Slovenia': '斯洛文尼亚',
#     'Sweden': '瑞典',
#     'Swaziland': '斯威士兰',
#     'Syria': '叙利亚',
#     'Chad': '乍得',
#     'Togo': '多哥',
#     'Thailand': '泰国',
#     'Tajikistan': '塔吉克斯坦',
#     'Turkmenistan': '土库曼斯坦',
#     'East Timor': '东帝汶',
#     'Trinidad and Tobago': '特里尼达和多巴哥',
#     'Tunisia': '突尼斯',
#     'Turkey': '土耳其',
#     'Tanzania': '坦桑尼亚',
#     'Uganda': '乌干达',
#     'Ukraine': '乌克兰',
#     'Uruguay': '乌拉圭',
#     'United States': '美国',
#     'Uzbekistan': '乌兹别克斯坦',
#     'Venezuela': '委内瑞拉',
#     'Vietnam': '越南',
#     'Vanuatu': '瓦努阿图',
#     'West Bank': '西岸',
#     'Yemen': '也门',
#     'South Africa': '南非',
#     'Zambia': '赞比亚',
#     'Zimbabwe': '津巴布韦',
#     'Comoros': '科摩罗'
# }

# map = Map(options.InitOpts(bg_color="#87CEFA",page_title='世界疫情分布')).\
#     add(series_name="世界疫情分布图",  #名称
#         data_pair=element,   #传入数据
#         is_map_symbol_show=False,  #不显示标记
#         maptype='world',   #地图类型
#         name_map=name_map,
#         )
# #设置全局配置项
# map.set_global_opts(visualmap_opts=options.VisualMapOpts(max_=1100000,is_piecewise=True,pieces=[
#                  {"min": 500000},
#                  {"min": 200000, "max": 499999},
#                  {"min": 100000, "max": 199999},
#                  {"min": 50000, "max": 99999},
#                  {"min": 10000, "max": 49999},
#                  {"max": 9999},]))
# #设置系列配置项
# map.set_series_opts(label_opts=options.LabelOpts(is_show=False))  #不显示国家名
# map.render('map.html')  #命名并保存







# #国际疫情数据
#     import json
#     import requests
#     import pandas as pd
#     from bs4 import BeautifulSoup
#     url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia?from=timeline&isappinstalled=0'
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
#         }
#     response = requests.get(url,headers = headers)
#     response.encoding = 'utf-8'
#     content = response.content.decode('utf-8')#以字节流形式打印网页源码
#     soup = BeautifulSoup(response.text,'lxml')
#     #爬取选择网页文档的内容
#     data = soup.find_all(name = 'script',attrs = {'id':'getListByCountryTypeService2true'})
#     #转为字符串
#     account = str(data)
#     account1 = account[95:-21]#切片截取从52到后面倒数21取到需要的数据
#     account1_json = json.loads(account1)
    
    
#     #提取数据到列表
#     id = []
#     continents = []
#     provinceName = []
#     currentConfirmedCount = []
#     confirmedCount = []
#     confirmedCountRank = []
#     suspectedCount = []
#     curedCount = []
#     deadCount = []
#     deadCountRank = []
#     deadRate = []
#     deadRateRank = []
#     print(len(account1_json))
#     i=0
#     for a in account1_json:
#         if 'id' in a:
#             id.append(a['id'])
#         else:
#             id.append('没有')
#         continents.append(a['continents'])
#         provinceName.append(a['provinceName'])
#         currentConfirmedCount.append(a['currentConfirmedCount'])
#         confirmedCount.append(a['confirmedCount'])
#         if 'confirmedCountRank' in a:
#             confirmedCountRank.append(a['confirmedCountRank'])
#         else:
#             confirmedCountRank.append('没有')
#         suspectedCount.append(a['suspectedCount'])
#         curedCount.append(a['curedCount'])
#         deadCount.append(a['deadCount'])
#         if 'deadCountRank' in a:
#             deadCountRank.append(a['deadCountRank'])
#         else:
#             deadCountRank.append('没有')
#         if 'deadRate' in a:
#             deadRate.append(a['deadRate'])
#         else:
#             deadRate.append('没有')
#         if 'deadRateRank' in a:
#             deadRateRank.append(a['deadRateRank'])
#         else:
#             deadRateRank.append('没有')
    
#     #转换成pandas数组
#     df = {
#         'id':pd.Series(id),
#         '所在大洲':pd.Series(continents),
#         '城市':pd.Series(provinceName),
#         '当前确诊':pd.Series(currentConfirmedCount),
#         '累计确诊':pd.Series(confirmedCount),
#         '确诊排名':pd.Series(confirmedCountRank),
#         '疑似病例':pd.Series(suspectedCount),
#         '治愈人数':pd.Series(curedCount),
#         '死亡人数':pd.Series(deadCount),
#         '死亡人数排名':pd.Series(deadCountRank),
#         '死亡率':pd.Series(deadRate),
#         '死亡率排名':pd.Series(deadRateRank)
#     }
#     pds = pd.DataFrame(df)
#     pds.to_excel('1.xlsx', index=False)


# #国际疫情
# import json
# import requests
# import pandas as pd
# from bs4 import BeautifulSoup
# url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia?from=timeline&isappinstalled=0'
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
#     }
# response = requests.get(url,headers = headers)
# response.encoding = 'utf-8'
# content = response.content.decode('utf-8')#以字节流形式打印网页源码
# soup = BeautifulSoup(response.text,'lxml')
# #爬取选择网页文档的内容
# data = soup.find_all(name = 'script',attrs = {'id':'getListByCountryTypeService2true'})
# #转为字符串
# account = str(data)
# account1 = account[95:-21]#切片截取从52到后面倒数21取到需要的数据
# account1_json = json.loads(account1)
# #提取数据到列表
# id = []
# continents = []
# provinceName = []
# currentConfirmedCount = []
# confirmedCount = []
# confirmedCountRank = []
# suspectedCount = []
# curedCount = []
# deadCount = []
# deadCountRank = []
# deadRate = []
# deadRateRank = []
# print(len(account1_json))
# i=0
# for a in account1_json:
#     if 'id' in a:
#         id.append(a['id'])
#     else:
#         id.append('没有')
#     continents.append(a['continents'])
#     provinceName.append(a['provinceName'])
#     currentConfirmedCount.append(a['currentConfirmedCount'])
#     confirmedCount.append(a['confirmedCount'])
#     if 'confirmedCountRank' in a:
#         confirmedCountRank.append(a['confirmedCountRank'])
#     else:
#         confirmedCountRank.append('没有')
#     suspectedCount.append(a['suspectedCount'])
#     curedCount.append(a['curedCount'])
#     deadCount.append(a['deadCount'])
#     if 'deadCountRank' in a:
#         deadCountRank.append(a['deadCountRank'])
#     else:
#         deadCountRank.append('没有')
#     if 'deadRate' in a:
#         deadRate.append(a['deadRate'])
#     else:
#         deadRate.append('没有')
#     if 'deadRateRank' in a:
#         deadRateRank.append(a['deadRateRank'])
#     else:
#         deadRateRank.append('没有')

# #转换成pandas数组
# df = {
#     'id':pd.Series(id),
#     '所在大洲':pd.Series(continents),
#     '城市':pd.Series(provinceName),
#     '当前确诊':pd.Series(currentConfirmedCount),
#     '累计确诊':pd.Series(confirmedCount),
#     '确诊排名':pd.Series(confirmedCountRank),
#     '疑似病例':pd.Series(suspectedCount),
#     '治愈人数':pd.Series(curedCount),
#     '死亡人数':pd.Series(deadCount),
#     '死亡人数排名':pd.Series(deadCountRank),
#     '死亡率':pd.Series(deadRate),
#     '死亡率排名':pd.Series(deadRateRank)
# }
# pds = pd.DataFrame(df)
# pds.to_excel('2.xlsx', index=False)














#国内疫情数据
    import requests
    import pandas as pd
    from bs4 import BeautifulSoup
    import re
    url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia?from=timeline&isappinstalled=0'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'
        }
    #省级正则表达式
    provinceName_re = re.compile(r'"provinceName":"(.*?)",')
    provinceShortName_re = re.compile(r'"provinceShortName":"(.*?)",')
    currentConfirmedCount_re = re.compile(r'"currentConfirmedCount":(.*?),')
    confirmedCount_re = re.compile(r'"confirmedCount":(.*?),')
    suspectedCount_re = re.compile(r'"suspectedCount":(.*?),')
    curedCount_re = re.compile(r'"curedCount":(.*?),')
    deadCount_re = re.compile(r'"deadCount":(.*?),')
    comment_re = re.compile(r'"comment":"(.*?)",')
    locationId_re = re.compile(r'"locationId":(.*?),')
    statisticsData_re = re.compile(r'"statisticsData":"(.*?)",')
    cities_re = re.compile(r'"cities":\[\{(.*?)\}\]')
    
    #市级正则表达式
    cityName_re = re.compile(r'"cityName":"(.*?)",')
    currentConfirmedCount_1_re = re.compile(r'"currentConfirmedCount":(.*?),')
    confirmedCount_1_re = re.compile(r'"confirmedCount":(.*?),')
    suspectedCount_1_re = re.compile(r'"suspectedCount":(.*?),')
    curedCount_1_re = re.compile(r'"curedCount":(.*?),')
    deadCount_1_re = re.compile(r'"deadCount":(.*?),')
    locationId_1_re = re.compile(r'"locationId":(.*?)\},')
    
    #爬虫爬取数据
    datas = requests.get(url,headers = headers)
    datas.encoding = 'utf-8'
    soup = BeautifulSoup(datas.text,'lxml')
    data = soup.find_all('script',{'id':'getAreaStat'})
    data = str(data)
    data_str = data[54:-23]
    
    #替换字符串内容，避免重复查找
    citiess = re.sub(cities_re,'8888',data_str)
    #查找省级数据
    provinceNames = re.findall(provinceName_re,citiess)
    provinceShortNames = re.findall(provinceShortName_re,citiess)
    currentConfirmedCounts = re.findall(currentConfirmedCount_re,citiess)
    confirmedCounts = re.findall(confirmedCount_re,citiess)
    suspectedCounts = re.findall(suspectedCount_re,citiess)
    curedCounts = re.findall(curedCount_re,citiess)
    deadCounts = re.findall(deadCount_re,citiess)
    comments = re.findall(comment_re,citiess)
    locationIds = re.findall(locationId_re,citiess)
    statisticsDatas = re.findall(statisticsData_re,citiess)
    
    
    #查找市级数据
    citiess_str1 = re.findall(cities_re,data_str)
    #将市级列表数据转为字符串，方便正则表达式查找
    citiess_str = str(citiess_str1)
    cityName = re.findall(cityName_re,citiess_str)
    currentConfirmedCount_1 = re.findall(currentConfirmedCount_1_re,citiess_str)
    confirmedCount_1 = re.findall(confirmedCount_1_re,citiess_str)
    suspectedCount_1 = re.findall(suspectedCount_1_re,citiess_str)
    curedCount_1 = re.findall(curedCount_1_re,citiess_str)
    deadCount_1 = re.findall(deadCount_1_re,citiess_str)
    
    # 省级数据转换为pandas数组
    df = {
        '地区代码':pd.Series(locationIds),
        '省':pd.Series(provinceNames),
        '省区短名':pd.Series(provinceShortNames),
        '当前确诊':pd.Series(currentConfirmedCounts),
        '累计确诊':pd.Series(confirmedCounts),
        '疑似确诊':pd.Series(suspectedCounts),
        '治愈人数':pd.Series(curedCounts),
        '死亡人数':pd.Series(deadCounts),
        '评论':pd.Series(comments),
        '统计数据区':pd.Series(statisticsDatas),
    }
    pds = pd.DataFrame(df)
    pds.to_excel('国内疫情统计表1.xlsx',index=True)

