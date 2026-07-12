import os
import datetime
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

mydb = MySQLDatabase(os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=3306,
    charset='utf8mb4'
)

print(mydb)


class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb


mydb.connect()
mydb.create_tables([TimelinePost])

NAV_ITEMS = [
    {"label": "Home", "url": "/"},
    {"label": "Hobbies", "url": "/hobbies"},
]

HENRIQUE_PROFILE = {
    "name": "Henrique",
    "title": "MLH Production Engineering Fellow",
    "photo": "henrique.jpg",
    "about": (
        "Hello, I'm Henrique Leite. I just finished my third year at the University of Western Ontario, "
        "where I'm pursuing an Honours Specialization in Computer Science with a heavy emphasis on "
        "Machine Learning and Data Science. My interests include back-end development, infrastructure, "
        "data engineering, and data science."
    ),
    "experiences": [
        {
            "role": "Software Developer (Amplify)",
            "organization": "Royal Bank of Canada",
            "description": "Building a patent-pending solution for US Cash management.",
        },
        {
            "role": "Software Engineer Intern",
            "organization": "Aurelis",
            "description": "Worked on developing property management software.",
        },
        {
            "role": "Data Analyst",
            "organization": "Scotiabank",
            "description": "Automated financial reporting and built data dashboards using VBA and Python. Used Power BI to streamline wealth analytics, client insights, and highlight portfolio exposure risk.",
        },
    ],
    "education": [
        {
            "school": "University of Western Ontario",
            "degree": "B.S. Honours Specialization in Computer Science",
            "description": "Focused on Machine Learning and Data Science.",
        },
    ],
    "hobbies": [
        {
            "name": "Guitar",
            "image": "guitar.jpg",
            "description": "I enjoy playing guitar, especially classic rock and metal. It's my go-to way to unwind and express myself through music.",
        },
        {
            "name": "Weightlifting",
            "image": "weightlifting.jpeg",
            "description": "Taking care of my health is a priority for me. Weightlifting keeps me disciplined, focused, and energized.",
        },
        {
            "name": "Travelling",
            "image": "travelling.jpg",
            "description": "I love exploring new places and experiencing different cultures. Every trip brings a fresh perspective and great memories.",
        },
    ],
    "places": [
        {"name": "Brasília (Hometown)", "lat": -15.7939, "lng": -47.8828},
        {"name": "São Paulo", "lat": -23.5505, "lng": -46.6333},
        {"name": "Rio de Janeiro", "lat": -22.9068, "lng": -43.1729},
        {"name": "Recife", "lat": -8.0476, "lng": -34.8770},
        {"name": "Salvador", "lat": -12.9714, "lng": -38.5124},
        {"name": "Goiânia", "lat": -16.6869, "lng": -49.2648},
        {"name": "Mexico City", "lat": 19.4326, "lng": -99.1332},
        {"name": "Cancún", "lat": 21.1619, "lng": -86.8515},
        {"name": "Miami", "lat": 25.7617, "lng": -80.1918},
        {"name": "San Francisco", "lat": 37.7749, "lng": -122.4194},
        {"name": "Boston", "lat": 42.3601, "lng": -71.0589},
        {"name": "New York", "lat": 40.7128, "lng": -74.0060},
        {"name": "Toronto", "lat": 43.6532, "lng": -79.3832},
        {"name": "Montreal", "lat": 45.5017, "lng": -73.5673},
        {"name": "Lisbon", "lat": 38.7223, "lng": -9.1393},
        {"name": "Albufeira", "lat": 37.0882, "lng": -8.2503},
        {"name": "Havana", "lat": 23.1136, "lng": -82.3666},
    ],
}


@app.route("/")
def index():
    return render_template(
        "index.html",
        title="Henrique",
        url=os.getenv("URL"),
        nav_items=NAV_ITEMS,
        profile=HENRIQUE_PROFILE,
    )


@app.route("/hobbies")
def hobbies():
    return render_template(
        "hobbies.html",
        title="Henrique's Hobbies",
        url=os.getenv("URL"),
        nav_items=NAV_ITEMS,
        profiles=[HENRIQUE_PROFILE],
    )


@app.route('/api/timeline_post', methods=['POST'])
def post_time_line_post():
    name = request.form['name']
    email = request.form['email']
    content = request.form['content']
    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return model_to_dict(timeline_post)


@app.route('/api/timeline_post', methods=['GET'])
def get_time_line_post():
    return {
        'timeline_posts': [
            model_to_dict(p)
            for p in
            TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }


@app.route('/api/timeline_post/<int:post_id>', methods=['DELETE'])
def delete_timeline_post(post_id):
    post = TimelinePost.get_by_id(post_id)
    post.delete_instance()
    return {'deleted': True, 'id': post_id}
