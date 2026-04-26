import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from lab2_scrapy.items import BookItem

class BooksSpider(CrawlSpider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    rules = (
        # قاعدة التنقل بين صفحات الفهرس
        Rule(LinkExtractor(restrict_css='li.next a'), follow=True),
        # قاعدة الدخول لصفحة الكتاب واستدعاء parse_book
        Rule(LinkExtractor(restrict_css='h3 a'), callback='parse_book', follow=False),
    )

    def parse_book(self, response):
        item = BookItem()

        item['title'] = response.css('h1::text').get()
        item['price'] = response.css('p.price_color::text').get()

        stock_parts = response.css('p.instock.availability::text').getall()
        item['stock'] = ' '.join(part.strip() for part in stock_parts if part.strip())

        rating_class = response.css('p.star-rating::attr(class)').get()
        if rating_class:
            item['rating'] = rating_class.replace('star-rating', '').strip()
        else:
            item['rating'] = 'No rating'

        breadcrumb = response.css('.breadcrumb a::text').getall()
        if len(breadcrumb) >= 2:
            item['category'] = breadcrumb[1]
        else:
            item['category'] = 'Unknown'

        item['url'] = response.url

        yield item