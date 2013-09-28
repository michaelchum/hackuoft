from scrapy.item import Item, Field


class Post(Item):

    title = Field()
    url = Field()
