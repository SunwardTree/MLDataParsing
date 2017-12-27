# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 20:12:24 2017

@author: Jack
"""
import json
import os

file_name = "./reviews_Books"

#如果文件存在 删除文件
if os.access(file_name + ".txt", os.F_OK):
    os.remove(file_name + ".txt")

filename = file_name + '.json'
output = open(file_name + ".txt", 'a')
with open(filename, 'rb') as f:
    count = 0;
    style_erro = 0;
    for line in f:
        jsonData = (((str(line).replace('b"','').replace("b'",'')).replace('\\n"','').replace("\\n'",'')).replace("'",'"').replace('"s ',"'s ")).replace('\\','');
        try:
            text = str(json.loads(jsonData))
        except:
            #print("JSON格式存在问题")
            style_erro = style_erro + 1
        else:
            output.write(text  + "\n")
        count = count + 1
    output.close()
print("一共 " + str(count) + " 条数据，有 " + str(style_erro) + " 条数据不能解析，占 " + str(style_erro/count))
        
    