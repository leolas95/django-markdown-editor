from django.test import TestCase

from martor_demo.app.models import Post


class PostTestCase(TestCase):
    def testPost(self):
        post = Post(title="asdads", description="desc", wiki="post wiki")
        self.assertEqual(post.title, "asdads")
        self.assertEqual(post.description, "desc")
        self.assertEqual(post.wiki, "post wiki")
