#!/usr/bin/env python3
"""Starts a Flask web application
The application listens on 0.0.0.0, port 5000
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """ Serves index page """
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0"))
