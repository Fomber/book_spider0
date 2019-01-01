import scrapy

class book_Spider(scrapy.Spider):
    name = 'book_spider'
    allowed_domains = ["books.toscrape.com"]
    start_urls = ['http://books.toscrape.com/catalogue/page-1.html']

    def parse(self, response):
        names = response.xpath('//li/article[@class="product_pod"]/h3/a')
        for book_name in names:
            print(book_name.attrib.get('title'))
            #w150121221155555552222225
            32222222222222
            313232
            31321
            3213
            13
            32
            32
            3
            32