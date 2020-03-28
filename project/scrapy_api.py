from scrapyd_api import ScrapydAPI
from project.settings import SCRAPY_URI

# create Scrapyd API Singleton
scrapyd = ScrapydAPI(SCRAPY_URI)
