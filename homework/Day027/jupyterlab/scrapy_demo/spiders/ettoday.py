import scrapy
from scrapy_demo.items import ScrapyDemoItem

class EttodaySpider(scrapy.Spider):
    name = 'ettoday'
    allowed_domains = ['www.ettoday.net']
    start_urls = ['https://www.ettoday.net/news/20201201/1866788.htm',
                  'https://www.ettoday.net/news/20201201/1866751.htm',
                  'https://www.ettoday.net/news/20201201/1866756.htm']

    def parse(self, response):
        item = ScrapyDemoItem()
        item['title'] = response.xpath('//title/text()').get()
        item['content'] = response.xpath('//div[@itemprop="articleBody"]/p/text()').getall()
        yield item

    
