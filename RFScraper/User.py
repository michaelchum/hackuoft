__author__ = 'ivanfer'

from PostList import PostList

class User:

    def __init__(self, email):
        self.key = email
        self.post_list = PostList()

    def addPost(self, post):
    
        self.post_list.addPost(post)

    def key(self):
        return self.key

    def post_list(self):
        return self.post_list

