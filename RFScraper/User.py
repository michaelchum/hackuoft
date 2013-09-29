__author__ = 'ivanfer'

from . import PostList

class User:

    def __init__(self, email):
        self.key = email
        self.post_list = PostList()

    def addPost(self, post):
    
        self.post_list.append(post)

    def key(self):
        return self.key

    def post_list(self):
        return self.post_list

