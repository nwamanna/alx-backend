#!/usr/bin/env python3
"""  to set Babel’s default locale ("en") and timezone ("UTC"). """
from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """the class to set languagues"""
    LANGUAGES = ["en", "fr"]
    # Set Babel's default locale to "en" and timezone to "UTC"
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# configure app with Config
app.config.from_object(Config)

# initialze babel
babel = Babel(app)


@app.route('/')
def index():
    """ return index page """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
