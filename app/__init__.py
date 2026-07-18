import os
import datetime
from flask import Flask, render_template, request
from dotenv import load_dotenv
from peewee import *
from playhouse.shortcuts import model_to_dict

load_dotenv()
app = Flask(__name__)

if os.getenv("TESTING") == "true":
    print("Running in test mode")
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(
        os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306,
    )

print(mydb)


class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb


mydb.connect(reuse_if_open=True)
mydb.create_tables([TimelinePost], safe=True)



NAV_ITEMS = [
    {"label": "Home", "url": "/"},
    {"label": "Kriti", "url": "/kriti"},
    {"label": "Henrique", "url": "/henrique"},
    {"label": "Hobbies", "url": "/hobbies"},
]

KRITI_PROFILE = {
    "name": "Kriti Behl",
    "title": "MLH Production Engineering Fellow",
    "photo": "kriti.jpg",
    "switch_url": "/henrique",
    "switch_name": "Henrique",
    "about": (
        "Hi, I'm Kriti Behl, I graduated with an M.S. in Computer & Information Science from University of Florida focused on "
        "backend systems, reliability and production engineering. I enjoy building systems "
        "that are easier to debug, operate and scale."
    ),
    "experiences": [
        {
            "role": "DevSecOps Intern",
            "organization": "Thales Group",
            "description": "Worked on backend services, observability, reliability tooling and production-focused service validation.",
        },
        {
            "role": "Graduate Assistant",
            "organization": "University of Florida",
            "description": "Supported student-facing operations, scheduling workflows and coordination across high-volume weekly activities.",
        },
        {
            "role": "Software Developer",
            "organization": "VLink",
            "description": "Building AI workflow tooling, retrieval quality checks, grounding behavior and production-focused RAG reliability workflows.",
        },
    ],
    "education": [
        {
            "school": "University of Florida",
            "degree": "M.S. in Computer & Information Science",
            "description": "Focused on software systems, backend engineering, distributed systems, and production reliability.",
        },
        {
            "school": "Jaypee Institute of Information Technology",
            "degree": "B.Tech in Computer Science and Engineering",
            "description": "Built a foundation in programming, data structures, algorithms, software engineering, and systems.",
        },
    ],
    "hobbies": [
        {
            "name": "Painting",
            "image": "hobby-painting.svg",
            "description": "I enjoy painting because it helps me slow down, think creatively and express ideas visually.",
        },
        {
            "name": "Travelling",
            "image": "hobby-travel.svg",
            "description": "I enjoy exploring new places, learning from different cultures and collecting memories from each trip.",
        },
        {
            "name": "Cooking New Dishes",
            "image": "hobby-cooking.svg",
            "description": "I like trying new recipes and experimenting with different flavors when I have time outside of work.",
        },
        {
            "name": "Open Source & GitHub Projects",
            "image": "hobby-opensource.svg",
            "description": "I enjoy contributing to open source and building GitHub projects around backend systems, reliability, workflow tooling and production engineering.",
        },
    ],
    "places": [
        {"name": "Chicago", "lat": 41.8781, "lng": -87.6298},
        {"name": "Miami", "lat": 25.7617, "lng": -80.1918},
        {"name": "Dallas", "lat": 32.7767, "lng": -96.7970},
        {"name": "San Francisco", "lat": 37.7749, "lng": -122.4194},
        {"name": "Singapore", "lat": 1.3521, "lng": 103.8198},
        {"name": "Jaipur", "lat": 26.9124, "lng": 75.7873},
        {"name": "Delhi", "lat": 28.7041, "lng": 77.1025},
        {"name": "Kerala", "lat": 10.8505, "lng": 76.2711},
        {"name": "Kolkata", "lat": 22.5726, "lng": 88.3639},
        {"name": "Phuket", "lat": 7.8804, "lng": 98.3923},
        {"name": "Krabi", "lat": 8.0863, "lng": 98.9063},
    ],
}

HENRIQUE_PROFILE = {
    "name": "Henrique",
    "title": "MLH Production Engineering Fellow",
    "photo": "henrique.jpg",
    "switch_url": "/kriti",
    "switch_name": "Kriti Behl",
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
        title="Kriti Behl",
        url=os.getenv("URL"),
        nav_items=NAV_ITEMS,
        profile=KRITI_PROFILE,
    )


@app.route("/henrique")
def henrique():
    return render_template(
        "index.html",
        title="Henrique",
        url=os.getenv("URL"),
        nav_items=NAV_ITEMS,
        profile=HENRIQUE_PROFILE,
    )


@app.route("/kriti")
def kriti():
    return render_template(
        "index.html",
        title="Kriti Behl",
        url=os.getenv("URL"),
        nav_items=NAV_ITEMS,
        profile=KRITI_PROFILE,
    )


@app.route("/hobbies")
def hobbies():
    return render_template(
        "hobbies.html",
        title="Team Hobbies",
        url=os.getenv("URL"),
        nav_items=NAV_ITEMS,
        profiles=[KRITI_PROFILE, HENRIQUE_PROFILE],
    )



@app.route("/api/timeline_post", methods=["POST"])
def post_timeline_post():
    name = request.form.get("name", "")
    email = request.form.get("email", "")
    content = request.form.get("content", "")

    if not name:
        return "Invalid name", 400
    if not content:
        return "Invalid content", 400
    if "@" not in email:
        return "Invalid email", 400

    timeline_post = TimelinePost.create(name=name, email=email, content=content)
    return model_to_dict(timeline_post)


@app.route("/api/timeline_post", methods=["GET"])
def get_timeline_post():
    return {
        "timeline_posts": [
            model_to_dict(p)
            for p in TimelinePost.select().order_by(TimelinePost.created_at.desc())
        ]
    }




@app.route("/timeline")
def timeline():
    return render_template("timeline.html", title="Timeline")

