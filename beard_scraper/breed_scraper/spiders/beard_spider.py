import scrapy


class BeardSpider(scrapy.Spider):
    name = 'breed'
    start_urls = [
        'https://catfishes.ru/porody-koshek/',
    ]

    def parse(self, response):
        cats_path = response.css('div.entry-content a::attr(href)').getall()
        for cat in cats_path:
            yield scrapy.Request(response.urljoin(cat), self.parse_cat)

    def parse_cat(self, response):
        cat = response.css('div.inside-article')
        yield {
            'catName': cat.css('header.entry-header h1.entry-title::text').get(),
            'catDescription': cat.css('div.entry-content p.has-drop-cap::text').get(),
            'cat_photo_src': cat.css('div.entry-content figure.wp-block-image img::attr(data-lazy-src)').get()  
        }
