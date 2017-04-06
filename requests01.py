# coding=utf-8
import requests
import re
from requests.packages import urllib3
from requests.auth import HTTPBasicAuth

# GET请求
"""
r = requests.get('https://www.baidu.com/')
print(type(r))
print(r.status_code)
print(r.text)
print(r.headers)
print(r.cookies)
print(r.url)
print(r.history)

data = {
    'name': 'neil',
    'age': 22
}
r = requests.get('http://httpbin.org/get',params=data)
print(type(r.text))
print(r.json())
print(type(r.json()))
"""

# 抓取网页
"""
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get('https://www.zhihu.com/explore',headers=headers)
pattern = re.compile(r'question_link.*?>(.*?)</a>',re.S)
titles = re.findall(pattern,r.text)
print(titles)
"""

# 抓取二进制数据
"""
r = requests.get('https://github.com/favicon.ico')
# r.content 二进制数据
with open('favicon.ico','wb') as f:
    f.write(r.content)
    f.close()
"""

# 基本POST请求
"""
data = {
    'name':'neil',
    'age':22
}
r = requests.post('http://httpbin.org/post',data=data)
print(r.text)
"""

# 文件上传
"""
files = {'file':open('favicon.ico','rb')}
r = requests.post('http://httpbin.org/post',files=files)
print(r.text)
"""

# cookie处理
# r = requests.get('https://www.baidu.com')
# for key,value in r.cookies.items():
#     print(key + '=' + value)
"""
cookies = 'd_c0="ABCCPjDF8AqPTtsuv33CI1ziBrEFH2v5Mfs=|1480736510"; _xsrf=fd2d0ab103ced1240e9a4c6951f2ada6; _zap=40a1513b-bda6-4ca8-88ff-5ce296f4d421; aliyungf_tc=AQAAAAwrylsk8g4As7a7y7BuneaY8/GY; q_c1=d95dd57c514f4fe6acb4a12025407c65|1489031322000|1480736510000; r_cap_id="ZTAzZWY1M2NiYTg3NDYzODhlMjAxNzdlZDRhYzhiOTY=|1490143930|f43b9a15788cb69fec773f40d9981b739c1d74e4"; cap_id="NDcyMWQ4NDIxM2EyNGI3NWE4NDUxMmJlMjRmZjM0MGY=|1490143930|4e4fcba9770f71527fddf9c793fc4456787eea7a"; z_c0=Mi4wQUFCQTNLWWdBQUFBRUlJLU1NWHdDaGNBQUFCaEFsVk53VmY1V0FDLWxrVkpKUHF4eGtUWm54Q3Eya3M4cUxCUjZB|1491452098|791120ba034c6e495300e9e7c00f6604edecda65; __utma=51854390.1591596562.1486345522.1490143934.1491452032.19; __utmb=51854390.0.10.1491452032; __utmc=51854390; __utmz=51854390.1491452032.19.18.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmv=51854390.100-1|2=registration_date=20131113=1^3=entry_date=20131113=1'
# 新建一个RequestCookieJar对象
jar = requests.cookies.RequestsCookieJar()
headers = {
    'Host':'www.zhihu.com',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
}
for cookie in cookies.split(';'):
    key, value = cookie.split('=',1)
    jar.set(key,value)
r = requests.get('http://www.zhihu.com',cookies=jar,headers=headers)
with open('zhihu.html','w') as f:
    f.write(r.text)
    f.close()
"""

# 会话维持 Session
"""
# requests.get('http://httpbin.org/cookies/set/number/123456789')
# r = requests.get('http://httpbin.org/cookies')
# print(r.text)
s = requests.Session()
s.get('http://httpbin.org/cookies/set/number/123456789')
r = s.get('http://httpbin.org/cookies')
print(r.text)
"""

# SSL证书验证
"""
# 忽略警告
urllib3.disable_warnings()
response = requests.get('https://www.12306.cn',verify=False)
print(response.status_code)
# 指定一个本地证书用作客户端证书
response = requests.get('https://www.12306.cn',cert=('/path/server.crt','/path/key'))
"""

# 代理设置
"""
proxies = {
    'http':'http://10.10.1.10:3128',
    'https':'http://10.10.1.10:1080',
}
requests.get('https://www.taobao.com',proxies=proxies)
# 若代理需要使用HTTP Basic Auth,可以使用类似http://user:password@host/
proxies = {
    'http':'http://user:password@10.10.1.10:3128/',
    'https':'https://user:password@10.10.1.10.1080',
}
requests.get('https://www.taobao.com',proxies=proxies)
"""

# 超时设置
"""
# 设置超时为1秒
r = requests.get('https://www.taobao.com',timeout=1)
# 实际上请求分为两个阶段，即连接和读取,如果要分别指定，就传入一个元组
r = requests.get('https://www.taobao.com',timeout=(1,5))
"""

# 身份认证
"""
# from requests.auth import HTTPBasicAuth
# r = requests.get('http://120.27.34.24:9001',auth=HTTPBasicAuth('user','123'))
# 简写
r = requests.get('http://120.27.34.24:9001',auth=('user','123'))
print(r.status_code)
# OAuth认证
# 需要安装oauth包。  --> pip3 install requests_oauthlib 
from requests_oauthlib import OAuth1
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET',
              'USER_OAUTH_TOKEN', 'USER_OAUTH_TOKEN_SECRET')
r = requests.get(url,auth=auth)
"""

