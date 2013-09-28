__author__ = 'ivanfer'


class PostList:
    """
    lists of posts for a single user.
    emails will be sent to the corresponding
    """

    def __init__(self, post):
        self.L = [post]

    def __iter__(self):
        return iter(self.L)

    def addPost(self, post):
        if post not in self.L:
            self.L.append(post)

    def next(self):
        pass

