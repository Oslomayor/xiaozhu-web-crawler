# 统计 http://bj.xiaozhu.com/ 网站上 13 个页面的房租信息
### 爬取的信息：标题、地址、价格、房东名称、房东性别和房东头像链接

10:57PM, Feb 6th, 2017

坑爹的发现在[这个页面上](http://bj.xiaozhu.com/search-duanzufang-p3-0/)  爬虫突然中止，刚开始以为 IP 被限制了

后来发现用 file.write() 打印这个字符串 '【限时特价】天安门♥故宫♥地铁旁精装三居整租' 报错    

> UnicodeEncodeError: 'gbk' codec can't encode character '\xbb' in position 8530: illegal multibyte sequence    

调试发现 '♥' 这个字符写入 txt 文件时报错，会使爬虫终止   

应该是跟特殊字符编码有关系，暂时不知道具体原因

原本这样写：

```python
file.write(key + ':' + data[key] + '\n')
```

采用 python 的异常处理机制，改为以下代码顺利工作：

```python
try:
	file.write(key + ':' + data[key] + '\n')
except UnicodeEncodeError:
	file.write('此处有非法字符' + '\n')
```

这是第一次比较完整地写了个爬虫，采用了 BeautifulSoup 库 和 html.parser 解析器， 接下来试试不同的解析器

   
