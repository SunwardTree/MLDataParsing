# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 20:12:24 2017

@author: Jack
"""
import json
import os

file_name = "./meta_Books"

#如果文件存在 删除文件
if os.access(file_name + ".txt", os.F_OK):
    os.remove(file_name + ".txt")
if os.access(file_name + "_erro.txt", os.F_OK):
    os.remove(file_name + "_erro.txt")

output = open(file_name + ".txt", 'a')
output_erro = open(file_name + "_erro.txt", 'a')
with open(file_name + ".json", 'rb') as f:
    count = 0;
    style_erro = 0;
    for line in f:
        #print("0 " + str(line))
        jsonData = ((str(line).replace('b"','').replace("b'",'')).replace('\\n"','').replace("\\n'",'').replace("\\r",'')).replace('\\','');
        try:
            text = str(json.loads(jsonData))
        except:
            #print("1 " + jsonData)
            try:
                jsonData = jsonData.replace("'",'"').replace('"s ',"'s ");
                #print("2 " + jsonData)
                text = str(json.loads(jsonData))
            except:
                output_erro.write(jsonData  + "\n")
                style_erro = style_erro + 1
            else:
                output.write(text  + "\n")
        else:
            output.write(text  + "\n")
        count = count + 1
    output.close()
print("一共 " + str(count) + " 条数据，有 " + str(style_erro) + " 条数据不能解析，占 " + str(style_erro/count))
        
    