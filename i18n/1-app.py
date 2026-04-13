#!/usr/bin/env python3
"""
Flask i18n app
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """
    Config class for Babel
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@app.route('/')
def main_page():
    """
    Main page of the app
    """
    return render_template('1-index.html'), 200


if __name__ == '__main__':
    app.run()
