# 6:34 PM, Feb 10th, 2018 @ hoome, Shangyu
# 不依赖 BeautifulSoup 库, 使用 re 模块提取价格
# urls:
# http://bj.xiaozhu.com/search-duanzufang-p1-0/
# http://bj.xiaozhu.com/search-duanzufang-p2-0/
# http://bj.xiaozhu.com/search-duanzufang-p3-0/
# http://bj.xiaozhu.com/search-duanzufang-p4-0/
# ...
# http://bj.xiaozhu.com/search-duanzufang-p13-0/
import re
import requests
import time

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

def get_prices(url):
    res = requests.get(url, headers)
    # 用正则表达式和 re 模块的 findall() 函数提取价格
    prices = re.findall('<span class="result_price">&#165;<i>(.*?)</i>起/晚</span>', res.text)
    for price in prices:
        print(price)

def main():
    # 列表推导式, 生成 13 个页面的 url
    urls = ['http://bj.xiaozhu.com/search-duanzufang-p{page}-0/'.format(page=page) for page in range(1, 14)]
    for url in urls:
        get_prices(url)
        time.sleep(1)

if __name__ == '__main__':
    main()

