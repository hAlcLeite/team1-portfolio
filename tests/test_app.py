import unittest
import os
os.environ['TESTING'] = 'true'

from app import app, mydb, TimelinePost


class AppTestCase(unittest.TestCase):
    def setUp(self):
        mydb.create_tables([TimelinePost])
        self.client = app.test_client()
    # had to add to drop tables 
    def tearDown(self):
        mydb.drop_tables([TimelinePost])

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "<title>Henrique</title>" in html
        # TODO Add more tests relating to the home page
        assert "Henrique" in html
        assert "Hobbies" in html  

    def test_timeline(self):
        response = self.client.get("/api/timeline_post")
        assert response.status_code == 200
        assert response.is_json
        json = response.get_json()
        assert "timeline_posts" in json
        assert len(json["timeline_posts"]) == 0
        # TODO Add more tests relating to the /api/timeline_post GET and POST apis
        post_response = self.client.post("/api/timeline_post", data={
            "name": "Post User",
            "email": "pu@example.com",
            "content": "Post Content"
        })
        assert post_response.status_code == 200
        post_json = post_response.get_json()
        assert post_json["name"] == "Post User"
        assert post_json["email"] == "pu@example.com"
        assert post_json["content"] == "Post Content"

        # Confirm it now shows up in the GET list
        get_response = self.client.get("/api/timeline_post")
        get_json = get_response.get_json()
        assert len(get_json["timeline_posts"]) == 1
        assert get_json["timeline_posts"][0]["name"] == "Post User"

    # TODO Add more tests relating to the timeline page
    def test_timeline_page_renders(self):
        response = self.client.get("/timeline")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "Timeline" in html
        assert "Create a Post" in html
        assert 'id="timeline-form"' in html
        assert 'id="posts-container"' in html
    
    def test_hobbies_page(self):
        response = self.client.get("/hobbies")
        assert response.status_code == 200
        html = response.get_data(as_text=True)
        assert "My Hobbies" in html
        assert "Guitar" in html
        assert "Weightlifting" in html
        assert "Travelling" in html

    def test_multiple_posts_ordered_newest_first(self):
        self.client.post("/api/timeline_post", data={
            "name": "1", "email": "1@example.com", "content": "1"
        })
        self.client.post("/api/timeline_post", data={
            "name": "2", "email": "2@example.com", "content": "2"
        })
        response = self.client.get("/api/timeline_post")
        posts = response.get_json()["timeline_posts"]
        assert posts[0]["name"] == "2"  #should be first now
        assert posts[1]["name"] == "1"
        
    # part 3 tests
    def test_malformed_timeline_post(self):
        # POST request missing name
        response = self.client.post("/api/timeline_post", data=
            {"email": "john@example.com", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid name" in html

        # POST request with empty content
        response = self.client.post("/api/timeline_post", data=
            {"name": "John Doe", "email": "john@example.com", "content": ""})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid content" in html

        # POST request with malformed email
        response = self.client.post("/api/timeline_post", data=
            {"name": "John Doe", "email": "not-an-email", "content": "Hello world, I'm John!"})
        assert response.status_code == 400
        html = response.get_data(as_text=True)
        assert "Invalid email" in html


if __name__ == '__main__':
    unittest.main()