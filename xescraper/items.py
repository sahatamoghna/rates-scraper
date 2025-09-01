import scrapy

class XeRawItem(scrapy.Item):
    # Keeping your existing item to minimize changes across the project
    date = scrapy.Field()
    currency = scrapy.Field()         # will always be 'USD' for this scraper
    currency_name = scrapy.Field()    # 'United States Dollar' from the table, if present
    rate = scrapy.Field()             # source -> USD
    inverse_rate = scrapy.Field()     # USD -> source
    source_country = scrapy.Field()   # one of GBP, AUD, EUR, CAD
