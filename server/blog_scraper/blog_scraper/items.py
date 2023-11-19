# # Define here the models for your scraped items
# #
# # See documentation in:
# # https://docs.scrapy.org/en/latest/topics/items.html

# import scrapy


# class BlogScraperItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

import scrapy

class BlogItem(scrapy.Item):
    Image_URL = scrapy.Field()
    Title = scrapy.Field()
    Date = scrapy.Field()
    Likes_Count = scrapy.Field()
