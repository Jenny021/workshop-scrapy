import scrapy

class EcommerceSpider(scrapy.Spider):
    name = 'ecommerce'
    allowed_domains = ['webscraper.io']
    start_urls = ['http://webscraper.io/test-sites/e-commerce/static']

    def parse(self, response):
        for info in response.css('div.thumbnail'):
            yield {
                'title': info.css('h4 a::attr(title)').get(),
                'detail_link': info.css('h4 a::attr(href)').get(),
                'description': info.css('p.description::text').get(),
                'price': info.css('h4::text').get(),
                'image': info.css('img').getall(),
                'rating': info.css('p::attr(data-rating)').get(),
                'review count': info.css('div.ratings p.pull-right::text').get()
            }
