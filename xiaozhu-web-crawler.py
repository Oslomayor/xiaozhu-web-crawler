# xiaozhu web crawler
# 5:14PM, Feb 5th, 2018 @ dormitory
# 统计 http://bj.xiaozhu.com/ 网站上 13 个页面的房租信息
# 爬取的信息：标题、地址、价格、房东名称、房东性别和房东头像链接

from bs4 import BeautifulSoup
import requests
import  time

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

# 子函数，获取每个页面中进入详细信息的链接
def getLinks(url):
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    # 获取详细页面的链接
    links = soup.select('#page_list > ul > li > a')
    for link in links:
        # 提取出链接, href 是进入详细页的链接
        href = link.get('href')
        getInfo(href)

def getInfo(href):
    global file
    res = requests.get(href, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    # 注意 select 方法得到的结果都是列表
    tittle = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > h4 > em')
    address = soup.select('body > div.wrap.clearfix.con_bg > div.con_l > div.pho_info > p > span')
    price = soup.select('#pricePart > div.day_l > span')
    hostname = soup.select('#floatRightBox > div.js_box.clearfix > div.w_240 > h6 > a')
    hostgender = soup.select('#floatRightBox > div.js_box.clearfix > div.member_pic > div')
    data = {
        'tittle': tittle[0].getText().strip(),
        'address': address[0].getText().strip(),
        'price': price[0].getText().strip(),
        'hostname': hostname[0].getText().strip(),
        'hostgender': judgeGender(hostgender[0].get('class')).strip()
    }
    print(data)
    for key in data.keys():
        file.write(key + ':' + data[key] + ' ')

def judgeGender(class_name):
    if class_name == ['member_ico1']:
        return '女'
    else:
        return '男'


def main():
    global file
    urls = ['http://bj.xiaozhu.com/search-duanzufang-p{page}-0/'.format(page=page) for page in range(1, 14)]
    file = open('E:/AllPrj/PyCharmPrj/py-crawler/results-xiaozhu-web-crawler.txt', 'w')
    for url in urls:
        print('page:{url}'.format(url=url))
        getLinks(url)
    file.close()


if __name__ == '__main__':
    main()