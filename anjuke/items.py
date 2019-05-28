# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class AnjukeItemXiaoQu(scrapy.Item):

    id = scrapy.Field()
    name = scrapy.Field()
    BuiltDate = scrapy.Field()
    WuYeFei = scrapy.Field()
    KaiFaShang = scrapy.Field()
    Address = scrapy.Field()
    Lvhua = scrapy.Field()
    WuYeGongSi = scrapy.Field()
    RongJiLv = scrapy.Field()

class AnjukeItemErshoufangInfo(scrapy.Item):

    url = scrapy.Field()
    xiaoqu_name = scrapy.Field()
    title = scrapy.Field()
    Total_Price = scrapy.Field()
    JianZhuMianJi = scrapy.Field()
    DanJia = scrapy.Field()

class AnjukeItemChuzuInfo(scrapy.Item):

    url = scrapy.Field()
    xiaoqu_name = scrapy.Field()
    price_per_month = scrapy.Field()
    HouseType = scrapy.Field()
    Zhuangxiu = scrapy.Field()
    MianJi = scrapy.Field()
    per_square_meter_price = scrapy.Field()
    title = scrapy.Field()
