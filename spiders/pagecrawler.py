from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class PageCrawler(CrawlSpider):
    name = 'pagecrawler'
    allowed_domains = ['www.amazon.com']
    start_urls = ['https://www.amazon.com']


    rules = (
        Rule(LinkExtractor(allow='.*'), callback='parse_f', follow=True),
    )

    def parse_f(self, response):
        print(response.css('title::text').get())