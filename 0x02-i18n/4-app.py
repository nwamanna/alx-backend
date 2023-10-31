#!/usr/bin/env python3
"""  to set Babel’s default locale ("en") and timezone ("UTC"). """
from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale():
    """ determie best language """
    locality = request.args.get('locale')
    if locality in app.config['LANGUAGES']:
        return locality
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """ return index page """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(debug=True)
