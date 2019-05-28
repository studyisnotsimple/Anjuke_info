# code:utf-8
from pyquery import PyQuery
import re
def parse(response):
    # 爬取当前页各个小区的url，为了接下来进去各个小区的详情页
    jpy = PyQuery(response.text)
    tr_list = jpy('#list-content > div > div.li-info > h3 > a').items()
    result = set()
    for tr in tr_list:
        result.add(tr.attr('href'))

    return result

def xiaoqu_detailInfo_parse(response):

    result = dict()

    jpy = PyQuery(response.text)

    result['name'] = jpy('body > div.contain-mod > div.p_1180.p_crumbs > a:nth-child(5)').text()
    result['BuiltDate'] = jpy('#basic-infos-box > dl > dd:nth-child(10)').text()
    result['WuYeFei'] = jpy('#basic-infos-box > dl > dd:nth-child(4)').text()
    result['KaiFaShang'] = jpy('#basic-infos-box > dl > dd:nth-child(18)').text()
    result['Address'] = jpy('body > div.contain-mod > div.community-nav-mod > div.comm-title > h1 > span').text()
    result['Lvhua'] = jpy('#basic-infos-box > dl > dd:nth-child(16)').text()
    result['WuYeGongSi'] = jpy('#basic-infos-box > dl > dd:nth-child(20)').text()
    result['RongJiLv'] = jpy('#basic-infos-box > dl > dd:nth-child(14)').text()
    result['id'] = re.findall(r'view/(\d*)', response.url)[0]

    return result

def get_ershoufang_detail_urllist(response):

    jpy = PyQuery(response.text)

    tr_list = jpy('body > div.contain-mod > div.g-module > div.m-main > ul > li > a > div.details > p.title > span').items()

    result = set()

    for each in tr_list:

        result.add(each.attr('href'))

    return result

def get_chuzu_detail_urllist(response):

    jpy = PyQuery(response.text)

    tr_list = jpy('body > div.contain-mod > div.g-module > div.m-main > ul > li > a > div.details > p.title > span').items()

    result = set()

    for each in tr_list:

        result.add(each.attr('href'))

    return result




def ershoufang_detail_Info(response):

    result = dict()

    jpy = PyQuery(response.text)

    result['url'] = response.url
    result['title'] = jpy('#content > div.clearfix.title-guarantee > h3').text()
    result['Total_Price'] = jpy('#content > div.wrapper > div.wrapper-lf > div.clearfix > div.basic-info.clearfix > span.light.info-tag > em').text()
    result['JianZhuMianJi'] = jpy('#content > div.wrapper > div.wrapper-lf > div.houseInfoBox > div > div.houseInfo-wrap > ul > li:nth-child(5) > div.houseInfo-content').text()
    result['DanJia'] = jpy('#content > div.wrapper > div.wrapper-lf > div.houseInfoBox > div > div.houseInfo-wrap > ul > li:nth-child(3) > div.houseInfo-content').text()
    result['xiaoqu_name'] = response.meta['xiaoqu_name']
    return result


def chuzu_detail_Info(response):

    result = dict()

    jpy = PyQuery(response.text)

    result['url'] = response.url
    result['price_per_month'] = jpy('body > div.wrapper > div.title-basic-info.clearfix > span.light.info-tag > em').text()
    result['HouseType'] = jpy('body > div.wrapper > div.mainbox.cf > div.lbox > ul > li:nth-child(2) > span.info').text()
    result['Zhuangxiu'] = jpy('body > div.wrapper > div.mainbox.cf > div.lbox > ul > li:nth-child(6) > span.info').text()
    result['MianJi'] = jpy('body > div.wrapper > div.title-basic-info.clearfix > span.info-tag.no-line > em').text()
    if result['MianJi']:
        result['per_square_meter_price'] = float(result['price_per_month'])/float(result['MianJi'])
    else:
        result['per_square_meter_price'] = '0'
    result['title'] = jpy('body > div.wrapper > h3').text()
    result['xiaoqu_name'] = response.meta['xiaoqu_name']

    return result
