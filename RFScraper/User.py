__author__ = 'ivanfer'


class User(object):

    def __init__(self, email):
        self.key = email
        self.post_list = PostList()

    def addPost(self, post):
        """

        @param post: a post to add to this user.
        """

        self.post_list.append(post)
