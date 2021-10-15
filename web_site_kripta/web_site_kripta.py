"""Kripta Ofiacial Web Site Flask"""


import os

from flask import Flask, render_template

# Constant Variables
BASE_DIR = os.getcwd()
TEMPLATES_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")

app = Flask(__name__, template_folder=TEMPLATES_DIR, static_folder=STATIC_DIR)


@app.route("/")
def landing_page():
    """Render a Landing Paga of Web Site"""
    return render_template("landing.html")


def create_app():
    """Return App"""
    return app
