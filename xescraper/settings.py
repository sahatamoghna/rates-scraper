BOT_NAME = "xescraper"

SPIDER_MODULES = ["xescraper.spiders"]
NEWSPIDER_MODULE = "xescraper.spiders"

LOG_LEVEL = "DEBUG"

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
    'xescraper.pipelines.MySQLPipeline': 300,
}

FEED_EXPORT_ENCODING = "utf-8"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
