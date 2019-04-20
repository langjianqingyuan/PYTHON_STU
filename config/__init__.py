""" 
@author: lileilei
@file: __init__.py 
@time: 2018/4/12 14:17 
"""  
import requests
res = requests.get("https://www.baidu.com/s?wd=python")
print(res.text)
print(res.encoding)
