# -*- coding: utf-8 -*-

# Scrapy settings for anjuke project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'anjuke'

SPIDER_MODULES = ['anjuke.spiders']
NEWSPIDER_MODULE = 'anjuke.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'anjuke (+http://www.yourdomain.com)'


ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5  # 下载延迟，使用上代理IP就可以延迟低点。
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:

# headers中 user-agent 一定要写，貌似就是看安居客反爬就看 user-agent和IP请求频率
DEFAULT_REQUEST_HEADERS = {
  # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  # 'Accept-Language': 'en',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
  # 'referer':'https://chongqing.anjuke.com/'

}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'anjuke.middlewares.AnjukeSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'anjuke.middlewares.ProxyMiddleware': 602,  # 设置602，是为了确保response先进入proxy中间件，
                                               # 后进入重定向中间件，不然proxy中间件不会起作用。
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'anjuke.pipelines.AnjukePipeline': 300,   # 管道，在管道中做判断，入库等操作
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False
# REDIRECT_ENABLED = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

MONGODB_HOST = '127.0.0.1'   # 本地数据库
MONGODB_PORT = '27017'    # 数据库端口
MONGODB_URI = 'mongodb://{}:{}'.format(MONGODB_HOST, MONGODB_PORT)
MONGODB_DATABASE = 'AnjukeInfo'  # 数据库名字


RETRY_TIMES = 6  # 有时代理不很好，重试次数多点，确保爬取数据完整
RETRY_HTTP_CODES = [400, 302, 503, 301]
RETRY_ENABLED = True
HTTPERROR_ALLOWED_CODES = [301, 302, 400]

SCHEDULER = 'scrapy_redis.scheduler.Scheduler'  # 更改去重对列为redis的去重队列

# Ensure all spiders share same duplicates filter through redis.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"   # 利用Redis去重

REDIS_URL = 'redis://localhost:6379'   # 配置连接
