#!/usr/bin/env python3
"""
Flask i18n app with mocked user login
"""
from flask import Flask, g, render_template, request
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    """Config class for Babel"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_TRANSLATION_DIRECTORIES = 'translations'


app = Flask(__name__)
app.config.from_object(Config)


def get_user():
    """Return user dictionary or None"""
    login_as = request.args.get('login_as')
    if login_as:
        try:
            return users.get(int(login_as))
        except (ValueError, TypeError):
            return None
    return None


@app.before_request
def before_request():
    """Find user if any and store it in flask.g.user"""
    g.user = get_user()


def get_locale():
    """Select locale from URL or request headers"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


babel = Babel(app, locale_selector=get_locale)


@app.route('/')
def main_page():
    """Main page"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run()
