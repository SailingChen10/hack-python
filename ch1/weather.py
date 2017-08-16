# 将读取的数据转换为字典格式
import sys
new_dict = {}
with open('weather_info.txt') as f:
    read_data = f.readlines()
    for line in read_data:
        words=line.split(",",1)
        #print(words)
        #print (isinstance(words,list))
        new_dict[words[0]]=words[1]
    #print(new_dict)

#查询
history_dict={}
user_input=input("请输入您要查询的地区：")
while user_input != 'exit':
    if user_input == 'help':
        print("输入城市名，返回该城市的天气数据；\n输入help，返回帮助文档；\n输入history，返回查询历史记录；\n输入exit，退出程序交互；\n")
    elif user_input == 'history':
        for k, v in history_dict.items():
            if v != '宝宝没找到\n':
                print(k,v)
    else:
        out_put=new_dict.get(user_input,"宝宝没找到\n")
        history_dict[user_input]=out_put
        print(out_put)

    user_input=input("请输入您要查询的地区：")
else:
    if user_input == 'exit':
        sys.exit(0)
