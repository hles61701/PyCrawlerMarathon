import scrapy


class EttodaySpider(scrapy.Spider):
    name = 'ettoday'
    allowed_domains = ['www.ettoday.net']
    start_urls = ['https://www.ettoday.net/news/20201201/1866788.htm', 'https://www.ettoday.net/news/20201201/1866751.htm', 'https://www.ettoday.net/news/20201201/1866756.htm']

    def parse(self, response):
        data = {}
        data['title'] = response.xpath('//title/text()').get()
        data['content'] = response.xpath('//div[@itemprop="articleBody"]/p/text()').getall()
        print(data)

        pass
