import requests
# 引入 requests，实现请求
from models.Blog import Blog

URL = 'http://localhost/api/blog/getbloglist'
# 输入在浏览器的网址
res = requests.get(URL)
# 发送 GET 方式的请求，并把返回的结果(响应)存储在 res 变量里头
# 答第二个问题，get() 方法需要输入一个网页链接
res.encoding = 'utf-8'

print(type(res))
print(type(res.text))