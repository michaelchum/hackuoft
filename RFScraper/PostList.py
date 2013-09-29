__author__ = 'ivanfer'


class PostList:
    """
    lists of posts for a single user.
    emails will be sent to the corresponding
    """

    def __init__(self):
        self.l = []

    def __iter__(self):
        return iter(self.l)

    def addPost(self, post):
        if post not in self.l:
            self.l.append(post)

    def next(self):
        self.l.next()

