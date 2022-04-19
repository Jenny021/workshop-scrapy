import scrapy

class EcommerceSpider(scrapy.Spider):
    name = 'ecommerce'
    allowed_domains = ['webscraper.io']
    start_urls = ['http://webscraper.io/']

    def parse(self, response):
        for info in response.css('div.thumbnail'):
            yield {
                'name': info.css('a.title::title').get()
            }
