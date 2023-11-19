import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from blog_scraper.items import BlogItem

class BlogSpider(CrawlSpider):
    name = 'blogspider'
    allowed_domains = ['rategain.com']
    start_urls = ['https://rategain.com/blog']

    rules = (
        Rule(LinkExtractor(allow=r'/page/\d+/'), callback='parse_blog', follow=True),
    )

    def parse_blog(self, response):
        articles = response.css('article.blog-item')
        for article in articles:
            item = BlogItem()
            item['Image_URL'] = article.css('div.img a::attr(href)').get()
            item['Title'] = article.css('div.content h6 a::text').get().strip()
            item['Date'] = article.css('div.blog-detail span::text').get().strip()
            item['Likes_Count'] = article.css('a.zilla-likes span::text').get().strip()
            yield item
