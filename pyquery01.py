from pyquery import PyQuery as pq

# 四种初始化方式
"""
1, 直接字符串 
doc = pq(("<html></html>")

2, lxml.etree
from lxml import etree
doc = pq(etree.fromstring("<html></html>"))

3, 直接传URL
doc = pq('http://www.baidu.com')

4, 传文件
doc = pq(filename='zhihu.html')
"""