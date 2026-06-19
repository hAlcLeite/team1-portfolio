import os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

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
        "Hi, I’m Kriti Behl, I graduated with an M.S. in Computer & Information Science from University of Florida focused on "
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
    "about": "Henrique’s profile uses the shared Team 1 portfolio structure.",
    "experiences": [],
    "education": [],
    "hobbies": [],
    "places": [],
}


@app.route("/")
def index():
    return render_template(
        "index.html",
        title="Team 1 Portfolio",
        url=os.getenv("URL"),
        nav_items=NAV_ITEMS,
        profile=HENRIQUE_PROFILE,
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
        title="Kriti's Hobbies",
        url=os.getenv("URL"),
        nav_items=NAV_ITEMS,
        profile=KRITI_PROFILE,
    )
