"""
    Title:  Simple flask application. It creates local server with draw text.

    Author: Mateusz Miernik

    Date            Version         Comment
    July 2021       1.0.0           Initial release

"""

from flask import Flask
from application_data import DATA
from random import choice

app = Flask(__name__)


@app.route('/')
def index_page():
    draw_text = choice(DATA)
    return f"<pre>{draw_text}<pre>"
