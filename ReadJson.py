# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 20:12:24 2017

@author: Jack
"""
import json
import os

file_name = "./reviews_Books"

# 如果文件存在 删除文件
if os.access(file_name + ".txt", os.F_OK):
    os.remove(file_name + ".txt")
if os.access(file_name + "_error.txt", os.F_OK):
    os.remove(file_name + "_error.txt")

output = open(file_name + ".txt", 'a')
output_error = open(file_name + "_error.txt", 'a')
with open(file_name + ".json", 'rb') as f:
    count = 0
    style_error = 0
    for line in f:
        # print("0 " + str(line))
        jsonData = ((str(line).replace('b"', '').replace("b'", '')).replace('\\n"', '').replace("\\n'", '')
                    .replace("\\r", '')).replace('\\', '')
        try:
            text = json.dumps(json.loads(jsonData))
        except:
            # print("1 " + jsonData)
            try:
                jsonData = jsonData.replace("'", '"').replace('"t ', "'t ").replace('"s ', "'s ").replace('s" ', "s' ")
                # print("2 " + jsonData)
                text = json.dumps(json.loads(jsonData))
            except:
                output_error.write(jsonData + "\n")
                style_error = style_error + 1
            else:
                output.write(text + "\n")
        else:
            output.write(text + "\n")
        count = count + 1
    output.close()
print(file_name + "一共 " + str(count) + " 条数据，有 " + str(style_error) + " 条数据不能解析，占 " + str(style_error/count))
