# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from scrapy.conf import settings
from pymongo.errors import DuplicateKeyError
from traceback import format_exc
from .items import AnjukeItemErshoufangInfo, AnjukeItemChuzuInfo, AnjukeItemXiaoQu


class AnjukePipeline(object):

    def __init__(self, mongo_url, mongo_db):
        self.mongo_uri = mongo_url
        self.mongo_db = mongo_db
        self.client = None
        self.db = None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGODB_URI'),   # 提取出了mongodb配置
            mongo_db=settings.get('MONGODB_DATABASE', 'items')
        )

    def open_spider(self, spider):
        _ = spider
        self.client = MongoClient(self.mongo_uri)  # 连接数据库
        self.db = self.client[self.mongo_db]
        self.db['AnjukeXiaoqu_info'].ensure_index('id', unique=True)  # 在表AnjukeXiaoqu_info中建立索引，并保证索引的唯一性
        self.db['Anjuke_Ershoufang_info'].ensure_index('url', unique=True)   # 在表Anjuke_Ershoufang_info中建立索引，并保证索引的唯一性
        self.db['Anjuke_chuzu_info'].ensure_index('url', unique=True)  # 在表Anjuke_chuzu_info中建立索引，并保证索引的唯一性

    def close_spider(self, spider):
        _ = spider
        self.client.close()  # 关闭数据库

    def process_item(self, item, spider):
        try:
            if isinstance(item, AnjukeItemXiaoQu):  # 判断是否是小区的item
                self.db['AnjukeXiaoqu_info'].update({'id': item['id']}, {'$set': item}, upsert=True)   # 通过id判断，有就更新，没有就插入
            if isinstance(item, AnjukeItemChuzuInfo):  # 判断是否是小区出租信息的item
                try:

                    self.db['Anjuke_chuzu_info'].update({'url': item['url']}, {'$set': item}, upsert=True)  # 通过url判断，有就更新，没有就插入
                except Exception as e:
                    print(e)   # 打印错误

            if isinstance(item, AnjukeItemErshoufangInfo):  # 判断是否是小区二手房信息的item
                try:

                    self.db['Anjuke_Ershoufang_info'].update({'url': item['url']}, {'$set': item}, upsert=True)

                except Exception as e:
                    print(e)  # 打印错误

        except DuplicateKeyError:
            spider.logger.debug(' duplicate key error collection')  # 唯一键冲突报错
        except Exception as e:
            _ = e
            spider.logger.error(format_exc())
        return item

