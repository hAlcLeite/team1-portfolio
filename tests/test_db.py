import unittest
from peewee import *

from app import TimelinePost

MODELS = [TimelinePost]

test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)

        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_timeline_post(self):
        first_post = TimelinePost.create(name='Elane', email='ee@example.com', content='Test 1- Elane!')
        assert first_post.id == 1
        second_post = TimelinePost.create(name='123541', email='abcdefg@example.com', content='Test 2!')
        assert second_post.id == 2


        # TODO: Get timeline posts and assert that they are correct
        posts = list(TimelinePost.select().order_by(TimelinePost.id))
        assert len(posts) == 2
        assert posts[0].name == 'Elane'
        assert posts[0].email == 'ee@example.com'
        assert posts[0].content == "Test 1- Elane!"
        assert posts[1].name == '123541'
        assert posts[1].email == 'abcdefg@example.com'
        assert posts[1].content == "Test 2!"

if __name__ == '__main__':
    unittest.main()