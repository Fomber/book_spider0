import scrapy
from urllib import parse

class book_Spider(scrapy.Spider):
    name = 'book_spider'
    allowed_domains = ["books.toscrape.com"]
    start_urls = ['http://books.toscrape.com/catalogue/page-1.html']

    def parse(self, response):
        names = response.xpath('//li/article[@class="product_pod"]/h3/a')
        for book_name in names:
            print(book_name.attrib.get('title'))
        next_url = response.xpath('//li[@class="next"]/a').attrib.get('href')
        if next_url:
            next_url = parse.urljoin(response.url,next_url)
            yield scrapy.Request(next_url,callback=self.parse)
        else:
            print('没有获取到next的地址')