# coding: utf-8
# Scrapy settings for properties project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#
import yaml
import os

BOT_NAME = 'EasyGoSpider'

SPIDER_MODULES = ['EasyGoSpider.spiders']
NEWSPIDER_MODULE = 'EasyGoSpider.spiders'

# Crawl responsibly by identifying yourself (and your website) on
# the user-agent
# USER_AGENT = 'EasyGoSpider (+http://www.yourdomain.com)'
header_path = os.path.join(os.path.split(__file__)[0], 'headers.yaml')
with open(header_path) as f:
    _headers = yaml.load(f)
DEFAULT_REQUEST_HEADERS = _headers

# Disable S3
AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""

DOWNLOADER_MIDDLEWARES = {
    "scrapy.contrib.downloadermiddleware.redirect.RedirectMiddleware": None,
    "EasyGoSpider.middleware.LocalRetryMiddleware": 302,
    "EasyGoSpider.middleware.UserAgentMiddleware": 300,
    "EasyGoSpider.middleware.CookiesMiddleware": 301,
}

ITEM_PIPELINES = {
    'EasyGoSpider.pipelines.MongoDBPipleline': 300,
}

COOKIES_DEBUG = False
LOG_LEVEL = 'INFO'
# LOG_FILE = "./logging.log"
LOG_ENCODING = "utf-8"
LOG_ENABLED = 1
LOG_STDOUT = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 16

DOWNLOAD_DELAY = 1

RETRY_ENABLED = 1
RETRY_TIMES = 10

CLOSESPIDER_TIMEOUT = 3600

# Don't filter
DUPEFILTER_CLASS = 'scrapy.dupefilters.BaseDupeFilter'

# CUSTOMIZE
REFRESH_COOKIES = 1  # 重新获取所有可用账号的COOKIE
CAPTCHA_RECOGNIZ = 2  # 1: 人工输入 2: 云打码

LAT_STEP = 50000  # Divided into N squares
LNG_STEP = 30000
LAT = [30519681, 30791396, LAT_STEP]  # orig * 100000
LNG = [103904185, 104205148, LNG_STEP]

COOKIE_INTERVAL = 1800  # 秒，同一账号成功获取COOKIE后，此时间内不再重复获取
MAX_FAIL_TIME = 20  # 每个账号失败次数上限，失败次数多有可能已经被禁

AUTO_CLEAR_PHANTOMJS = 1
