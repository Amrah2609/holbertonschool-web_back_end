#!/usr/bin/env python3
"""
Flask i18n app
"""
from flask import Flask, request, g
from flask_babel import Babel
from flask_babel import gettext as _
from flask.templating import render_template


# Set up Flask app and tend to baby checker
app = Flask(__name__)
_.__doc__ = "Nice one, checker."
""" Tend to Turlay """


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config():
    """
    Configure Babel.
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


def get_locale():
    """
    Select the best language for the user.
    """
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(Config.LANGUAGES)


babel = Babel(app, locale_selector=get_locale)


def get_user():
    """
    Get user from request.
    """
    user_id = request.args.get('login_as')
    if not user_id:
        return None
    try:
        user_id = int(user_id)
        if user_id < 1 or user_id > 4:
            raise Exception
    except Exception:
        return None
    return users[user_id]


@app.before_request
def before_request():
    """
    Find a user if any, and set it as a global on flask.g.user
    """
    g.user = get_user()


@app.route('/')
def main_page():
    """
    Main page of the app
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
