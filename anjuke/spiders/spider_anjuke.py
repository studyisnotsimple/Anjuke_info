# -*- coding: utf-8 -*-

from scrapy.http import Request
from pyquery import PyQuery
from traceback import format_exc
from ..utils.parse import parse,\
        xiaoqu_detailInfo_parse, get_ershoufang_detail_urllist, get_chuzu_detail_urllist,\
        ershoufang_detail_Info, chuzu_detail_Info


from scrapy_redis.spiders import RedisSpider

from ..items import AnjukeItemXiaoQu, AnjukeItemChuzuInfo, AnjukeItemErshoufangInfo

class SpiderAnjukeSpider(RedisSpider):

    xiaoqu_url_list_count = 2      # 设置小区翻页页数
    ershoufang_url_list_count = 2  # 设置二手房翻页页数
    chuzu_url_list_count = 2       # 设置出租房翻页页数

    name = 'spider_anjuke'
    allowed_domains = ['anjuke.com']
    host = 'chongqing'             # 此处可以手动修改为想要爬取的城市
    xingzhengqu_code = ['yubei']   # 此处可以修改为想要爬取的行政区

    def start_requests(self):

        start_urls = ['https://{}.anjuke.com/community/{}/'.format(self.host, code) for code in self.xingzhengqu_code]
        for url in start_urls:
            headers1 = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
                'x-requested-with': 'XMLHttpRequest',

                'pragma': 'no-cache',
                ':authority': 'chongqing.anjuke.com',
                'cookie': 'sessid=2FF128CF-5BAC-E97C-C47C-15F22510F568; aQQ_ajkguid=E0708B3B-01E3-290E-C70B-0DC792BFEC02; lps=http%3A%2F%2Fwww.anjuke.com%2F%3Fpi%3DPZ-baidu-pc-all-biaoti%7Chttp%3A%2F%2Fbzclk.baidu.com%2Fadrc.php%3Ft%3D06KL00c00f7WWws0JbN600PpAsjmZVwT00000KUv7dC00000VSQ6P_.THvs_oeHEtY0UWY1rH0YnW0dr7tkgvq-UNqbusK15yFhmywbmvNhnj0snH03nyc0IHY0mHdL5iuVmv-b5HnznHmvPHDsPHfhTZFEuA-b5HDv0ARqpZwYTZnlQzqLILT8my4JIyV-QhPEUitOTAbqR7CVmh7GuZRVTAnVmyk_QyFGmyqYpfKWThnqn1fkn1D%26tpl%3Dtpl_11534_19640_15673%26l%3D1511519766%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E5%2525AE%252589%2525E5%2525B1%252585%2525E5%2525AE%2525A2-%2525E5%252585%2525A8%2525E6%252588%2525BF%2525E6%2525BA%252590%2525E7%2525BD%252591%2525EF%2525BC%25258C%2525E6%252596%2525B0%2525E6%252588%2525BF%252520%2525E4%2525BA%25258C%2525E6%252589%25258B%2525E6%252588%2525BF%252520%2525E6%25258C%252591%2525E5%2525A5%2525BD%2525E6%252588%2525BF%2525E4%2525B8%25258A%2525E5%2525AE%252589%2525E5%2525B1%252585%2525E5%2525AE%2525A2%2525EF%2525BC%252581%2526xp%253Did%28%252522m3216651054_canvas%252522%29%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D173%26ie%3DUTF-8%26f%3D8%26ch%3D1%26tn%3D39042058_1_oem_dg%26wd%3D%25E5%25AE%2589%25E5%25B1%2585%25E5%25AE%25A2%26oq%3D%25E5%25AE%2589%25E5%25B1%2585%25E5%25AE%25A2%26rqlang%3Dcn; ctid=20; twe=2; __xsptplusUT_8=1; _ga=GA1.2.1704013938.1557405404; _gid=GA1.2.1293415059.1557405404; _gat=1; wmda_uuid=e62d62c7d77cbda05aa079e31a108c8a; wmda_new_uuid=1; wmda_session_id_6289197098934=1557405404752-1f9d5e3b-58fd-db3a; wmda_visited_projects=%3B6289197098934; 58tj_uuid=e0cf84bd-3041-463f-baed-ec3754c89a38; init_refer=http%253A%252F%252Fbzclk.baidu.com%252Fadrc.php%253Ft%253D06KL00c00f7WWws0JbN600PpAsjmZVwT00000KUv7dC00000VSQ6P_.THvs_oeHEtY0UWY1rH0YnW0dr7tkgvq-UNqbusK15yFhmywbmvNhnj0snH03nyc0IHY0mHdL5iuVmv-b5HnznHmvPHDsPHfhTZFEuA-b5HDv0ARqpZwYTZnlQzqLILT8my4JIyV-QhPEUitOTAbqR7CVmh7GuZRVTAnVmyk_QyFGmyqYpfKWThnqn1fkn1D%2526tpl%253Dtpl_11534_19640_15673%2526l%253D1511519766%2526attach%253Dlocation%25253D%252526linkName%25253D%252525E6%252525A0%25252587%252525E5%25252587%25252586%252525E5%252525A4%252525B4%252525E9%25252583%252525A8-%252525E6%252525A0%25252587%252525E9%252525A2%25252598-%252525E4%252525B8%252525BB%252525E6%252525A0%25252587%252525E9%252525A2%25252598%252526linkText%25253D%252525E5%252525AE%25252589%252525E5%252525B1%25252585%252525E5%252525AE%252525A2-%252525E5%25252585%252525A8%252525E6%25252588%252525BF%252525E6%252525BA%25252590%252525E7%252525BD%25252591%252525EF%252525BC%2525258C%252525E6%25252596%252525B0%252525E6%25252588%252525BF%25252520%252525E4%252525BA%2525258C%252525E6%25252589%2525258B%252525E6%25252588%252525BF%25252520%252525E6%2525258C%25252591%252525E5%252525A5%252525BD%252525E6%25252588%252525BF%252525E4%252525B8%2525258A%252525E5%252525AE%25252589%252525E5%252525B1%25252585%252525E5%252525AE%252525A2%252525EF%252525BC%25252581%252526xp%25253Did%28%25252522m3216651054_canvas%25252522%29%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FDIV%2525255B1%2525255D%2525252FH2%2525255B1%2525255D%2525252FA%2525255B1%2525255D%252526linkType%25253D%252526checksum%25253D173%2526ie%253DUTF-8%2526f%253D8%2526ch%253D1%2526tn%253D39042058_1_oem_dg%2526wd%253D%2525E5%2525AE%252589%2525E5%2525B1%252585%2525E5%2525AE%2525A2%2526oq%253D%2525E5%2525AE%252589%2525E5%2525B1%252585%2525E5%2525AE%2525A2%2526rqlang%253Dcn; new_uv=1; new_session=0; als=0; __xsptplus8=8.1.1557405405.1557405416.3%232%7Cbzclk.baidu.com%7C%7C%7C%25E5%25AE%2589%25E5%25B1%2585%25E5%25AE%25A2%7C%23%23gPF4NCCLDwb85Ws6YGgCx7wU7Ishq9Mh%23',

            }
            count = self.xiaoqu_url_list_count    # 爬取行政区中count页数的小区urllist
            yield Request(url,
                          headers=headers1,
                          dont_filter=True,
                          meta={'count': count},  # 用meta将count 传递下去
                          )

    def parse(self, response):
        url_list = parse(response)

        for url in url_list:

            yield Request(url,
                          callback=self.xiaoqu_detail_pag,
                          errback=self.error_back,
                          priority=4,
                          dont_filter=True,

                          )

        count = response.meta['count']-1    # 获取到一页小区urllist后，count值就减一，然后判断是否翻页。然后翻页处理，
        jpy = PyQuery(response.text)
        next_page = jpy('body > div.w1180 > div.maincontent > div.page-content > div > a.aNxt').attr('href')  # selector定位下一页url

        if count > 0 and next_page:

            yield Request(next_page,
                          callback=self.parse,
                          errback=self.error_back,
                          priority=4,
                          dont_filter=True,
                          meta={'count': count},    # 继续传递count，计数不能停
                          )

        else:
            pass

    def xiaoqu_detail_pag(self, response):

        data = xiaoqu_detailInfo_parse(response)

        item = AnjukeItemXiaoQu()

        item.update(data)

        yield item

        # 进入二手房
        url = 'https://{}.anjuke.com/community/props/sale/{}/'.format(self.host, item['id'])

        ershoufang_count = self.ershoufang_url_list_count
        yield Request(url,
                      callback=self.get_ershoufang_list,
                      errback=self.error_back,
                      meta={'id': item['id'], 'count': ershoufang_count, 'xiaoqu_name': item['name']},
                      priority=3,
                      dont_filter=True,
                      )
        # 进入出租房
        url_ = 'https://{}.anjuke.com/community/props/rent/{}'.format(self.host, item['id'])

        chuzufang_count = self.chuzu_url_list_count
        yield Request(url_,
                      callback=self.get_chuzu_list,
                      errback=self.error_back,
                      meta={'id': item['id'], 'count': chuzufang_count, 'xiaoqu_name': item['name']},
                      priority=2,
                      dont_filter=True,
                      )

    def get_ershoufang_list(self, response):
        print(response.url)

        urllist = get_ershoufang_detail_urllist(response)

        for url in urllist:

            yield Request(url,
                          callback=self.ershoufang_detail_page,
                          errback=self.error_back,
                          priority=1,
                          meta={'id': response.meta['id'], 'xiaoqu_name': response.meta['xiaoqu_name']},
                          dont_filter=True,
                          )
        count = response.meta['count'] - 1
        jpy = PyQuery(response.text)
        next_page = jpy('body > div.contain-mod > div.g-module > div.m-main > div.m-page > div > a.aNxt').attr('href')
        if count > 0 and next_page:

            yield Request(
                    next_page,
                    callback=self.get_ershoufang_list,
                    errback=self.error_back,
                    priority=1,
                    dont_filter=True,
                    meta={'count': count, 'id': response.meta['id'], 'xiaoqu_name': response.meta['xiaoqu_name']},
                         )

    def ershoufang_detail_page(self, response):

        data = ershoufang_detail_Info(response)

        item = AnjukeItemErshoufangInfo()

        item.update(data)

        yield item

    def get_chuzu_list(self, response):

        urllist = get_chuzu_detail_urllist(response)
        for url in urllist:
            yield Request(
                          url,
                          callback=self.chuzu_detail_page,
                          errback=self.error_back,
                          priority=1,
                          meta={'id': response.meta['id'], 'xiaoqu_name': response.meta['xiaoqu_name']},
                          dont_filter=True,
                          )

        count = response.meta['count'] - 1

        jpy = PyQuery(response.text)

        next_page = jpy('body > div.contain-mod > div.g-module > div.m-main > div.m-page > div > a.aNxt').attr('href')

        if count > 0 and next_page:
            yield Request(next_page,
                          callback=self.get_chuzu_list,
                          errback=self.error_back,
                          priority=1,
                          dont_filter=True,
                          meta={'count': count, 'id': response.meta['id'], 'xiaoqu_name': response.meta['xiaoqu_name']},
                          )

    def chuzu_detail_page(self, response):

        data = chuzu_detail_Info(response)

        item = AnjukeItemChuzuInfo()

        item.update(data)

        yield item

    def error_back(self, e):
        _ = e
        self.logger.error(format_exc())  # 这种设置报错更详细
