import scrapy

class EcommerceSpider(scrapy.Spider):
    name = 'ecommerce'
    allowed_domains = ['webscraper.io']
    start_urls = [
        'http://webscraper.io/test-sites/e-commerce/static',
        'https://webscraper.io/test-sites/e-commerce/static/computers/laptops',
        'https://webscraper.io/test-sites/e-commerce/static/computers/tablets',
        'https://webscraper.io/test-sites/e-commerce/static/phones/touch'
        ]

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
        next_page = response.css('li.page-item a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
