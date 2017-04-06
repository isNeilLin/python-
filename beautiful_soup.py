import bs4
from bs4 import BeautifulSoup
html = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">this is a story</p>
<p class="story">this is another story</p>"""
soup = BeautifulSoup(html,'html.parser')
# 还可以用本地 HTML 文件来创建对象
# soup = BeautifulSoup(open(zhihu.html))
# print(soup.prettify)

# soup 对象本身比较特殊，它的 name 即为 [document]，对于其他内部标签，输出的值便为标签本身的名称。

print(soup.title.name)
print(soup.p.attrs)
print(soup.a.attrs)
# 单独获取某个属性
print(soup.a['href'])

# 对这些属性和内容等等进行修改,删除
# soup.p['class'] = 'newClass'
# del soup.p['class']

# 获取标签内部的文字,用 .string 即可.它的类型是一个 NavigableString，翻译过来叫 可以遍历的字符串
print(soup.p.string)

# Comment Comment 对象是一个特殊类型的 NavigableString 对象，其实输出的内容不包括注释符号
print(soup.a)
print(type(soup.a.string))
if type(soup.a.string) == bs4.element.Comment:
    print(soup.a.string)

# 遍历文档树
# .contents  tag 的 .content 属性可以将tag的子节点以列表的方式输出
# .children 它返回的不是一个 list，不过我们可以通过遍历获取所有子节点。
# .descendants .descendants 属性可以对所有tag的子孙节点进行递归循环，和 children类似，需要遍历获取其中的内容。
# .string 如果一个标签里面没有标签了，那么 .string 就会返回标签里面的内容。
# 如果标签里面只有唯一的一个标签了，那么 .string 也会返回最里面的内容,如果tag包含了多个子节点,tag就无法确定，输出结果是 None

# 多个内容
# .strings 获取多个内容，不过需要遍历获取
# for string in soup.body.strings:
#     print(string)

# .stripped_strings ,使用 .stripped_strings 可以去除多余空白内容
# for string in soup.body.stripped_strings:
#     print(string)

# 搜索文档树
# findall(name,attrs,recursive,text,**kwargs)
# find_all() 方法搜索当前tag的所有tag子节点,并判断是否符合过滤器的条件
# name 参数可以查找所有名字为 name 的tag,字符串对象会被自动忽略掉
# recursive 调用tag的 find_all() 方法时,Beautiful Soup会检索当前tag的所有子孙节点,
# 如果只想搜索tag的直接子节点,可以使用参数 recursive=False .

# CSS选择器
# select() select 方法返回的结果都是列表形式，可以遍历形式输出，然后用 get_text() 方法来获取它的内容。
