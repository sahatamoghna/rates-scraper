BOT_NAME = "xescraper"

SPIDER_MODULES = ["xescraper.spiders"]
NEWSPIDER_MODULE = "xescraper.spiders"

LOG_LEVEL = "DEBUG"

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'xescraper.pipelines.MySQLPipeline': 300,
}

# If you later add proxy auth middleware, uncomment and configure:
# DOWNLOADER_MIDDLEWARES = {
#     'xescraper.middlewares.ProxyAuthMiddleware': 100,
#     'scrapy.downloadermiddlewares.retry.RetryMiddleware': 90,
#     'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
# }

FEED_EXPORT_ENCODING = "utf-8"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
