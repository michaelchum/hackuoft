__author__ = 'ivanfer'


class Post:
    """
    we want scrapy to give us objects like these that we can iterate over
    """

    def __init__(self, title , url, deal=None):
        self.title = title
        self.url = url
        if deal is not None:
            self.deal_link = deal

    def __eq__(self, other):
        return self.url == other.url

