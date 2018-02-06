# 统计 http://bj.xiaozhu.com/ 网站上 13 个页面的房租信息
## 爬取的信息：标题、地址、价格、房东名称、房东性别和房东头像链接
坑爹的发现在[这个页面上](http://bj.xiaozhu.com/search-duanzufang-p3-0/)  
用 file.write() 打印这个字符串 '【限时特价】天安门♥故宫♥地铁旁精装三居整租' 报错  
-> UnicodeEncodeError: 'gbk' codec can't encode character '\xbb' in position 8530: illegal multibyte sequence    
'♥' 这个字符写入 txt 文件时报错，会使爬虫终止  
-
统计短租 网站上 13 个页面的房租信息  
IP 被封了，统计结果暂时还没出来  

   
