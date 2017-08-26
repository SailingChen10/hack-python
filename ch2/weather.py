#coding:utf-8
import requests,sys,json
#知心天气API
def fetchWeather(location):
    result = requests.get('https://api.seniverse.com/v3/weather/now.json', params={
        'key': 'epckoym47tehbdex',
        'location': location,
        'language': 'zh-Hans',
        'unit': 'c'
    }, timeout=20)
    return result.json()

#天气数据展示
def weatherPresentation(weather_dict):
    text = weather_dict['results'][0]['now']['text']
    temp = weather_dict['results'][0]['now']['temperature']
    last_update = weather_dict['results'][0]['last_update']
    weather = "%s 的天气为%s, 温度为 %s摄氏度.\n更新时间: %s\n"%(user_input,text,temp,last_update)
    return weather

# 查询逻辑
history_list=[]
while True:
    user_input=input("请输入您要查询的城市名称：")
    if user_input == 'help':
        print ("输入城市名，返回该城市的天气数据；\n输入help，返回帮助文档；\n输入history，返回查询历史记录；\n输入exit，退出程序交互；\n")
    elif user_input == 'history':
        for k in history_list:
            print(k)
    elif user_input == 'exit':
        break
    else:
        result_one=fetchWeather(user_input)
        final_result=weatherPresentation(result_one)
        history_list.append(final_result)
        print(final_result)
