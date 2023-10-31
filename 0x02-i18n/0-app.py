#!/usr/bin/env python3
"""  basic Flask app that creates a single / route and """
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    """ return index page """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(debug=True)
