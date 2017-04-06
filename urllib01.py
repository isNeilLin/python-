from urllib import request, parse
from urllib.robotparser import RobotFileParser
import ssl
import http.cookiejar
"""
# 普通GET请求
with request.urlopen("http://www.baidu.com/") as f:
    data = f.read()
    print('Status:',f.status,f.reason)
    for k,v in f.getheaders():
        print('%s: %s' % (k,v))
    # print('Data: ',data.decode('utf-8'))

print('Login weibo.cn...')
email = input('Email:')
password = input('Password:')
# 验证SSL
gcontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
# POST请求的data
login_data = parse.urlencode([
    ('username',email),
    ('password',password),
    ('entry','mweibo'),
    ('client_id',''),
    ('savestate','1'),
    ('ec',''),
    ('pagerefer','https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])
req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin','https://passport.weibo.cn')
req.add_header('User-Agent','Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer','https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req,context=gcontext,data=login_data.encode('utf-8')) as f:
    print('Status:',f.status,f.reason)
    print('Data:',f.read().decode('utf-8'))

proxyHandler 代理的设置
一个网站它会检测某一段时间某个IP 的访问次数，如果访问次数过多，它会禁止你的访问。
所以可以设置一些代理服务器来帮助你做工作，每隔一段时间换一个代理
proxy_handler = request.ProxyHandler({'http':'http://www.example.com:3128/'})
proxy_auth_handler = request.ProxyBasicAuthHandler()
proxy_auth_handler.add_password('realm','host','username','password')
opener = request.build_opener(proxy_handler,proxy_auth_handler)
with opener.open('http://www.example.com/login.html') as f:
    pass

# URLError异常处理
req = request.Request('http://blog.csdn.net/cqcre')
try:
    request.urlopen(req)
except request.HTTPError as e:
    print(e.code)
except request.URLError as e:
    if hasattr(e,'reason'):
        print(e.reason)
else:
    print('OK')
"""
# 获取Cookie保存到变量
# 声明一个CookieJar对象实例来保存cookie
# cookie = http.cookiejar.CookieJar()
# # 利用urllib库的HTTPCookieProcessor对象来创建cookie处理器
# handler = request.HTTPCookieProcessor(cookie)

# opener = request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name+'='+item.value)

# 保存成文本形式
filename = 'cookie.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# handler = request.HTTPCookieProcessor(cookie)
# opener = request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# cookie.save(ignore_discard=True,ignore_expires=True)

# 从文件读取cookie
cookie = http.cookiejar.MozillaCookieJar()
cookie.load(filename,ignore_discard=True,ignore_expires=True)
handler = request.HTTPCookieProcessor(cookie)
opener = request.build_opener(handler)
response = opener.open('http://www.baidu.com',timeout=50)
# print(response.read().decode('utf-8'))

# parse.urlparse
result = parse.urlparse('http://www.baidu.com/index.html;user?id=5#comment')
# output: ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')

# parse.urljoin
print(parse.urljoin('http://www.baidu.com', 'FAQ.html'))
# http://www.baidu.com/FAQ.html
print(parse.urljoin('http://www.baidu.com', 'https://cuiqingcai.com/FAQ.html'))
# https://cuiqingcai.com/FAQ.html
print(parse.urljoin('http://www.baidu.com/about.html', 'https://cuiqingcai.com/FAQ.html?question=2'))
# https://cuiqingcai.com/FAQ.html?question=2
print(parse.urljoin('http://www.baidu.com', '?category=2#comment'))
# http://www.baidu.com?category=2#comment

# urllib.robotparser
rp = RobotFileParser()
rp.parse(request.urlopen('http://www.jianshu.com/robots.txt').read().decode('utf-8').split('\n'))
print(rp.can_fetch('*','http://www.jianshu.com/p/b67554025d7d'))
print(rp.can_fetch('*','http://www.jianshu.com/search?q=python&page=1&type=collections'))