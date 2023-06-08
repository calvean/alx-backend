#!/usr/bin/env python3
"""
Starts a Flask web application and use gettext
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext as _
import pytz

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Language and locale configs """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """ Returns the user dictionary or None if user_id not found """
    return users.get(user_id)


@babel.localeselector
def get_locale():
    """ Selects the best language based on user's preferences """
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale

    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']

    locale = request.accept_languages.best_match(app.config['LANGUAGES'])
    if locale:
        return locale

    return app.config['BABEL_DEFAULT_LOCALE']


@babel.timezoneselector
def get_timezone():
    """ Selects the best time zone based on user's preferences """
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.UnknownTimeZoneError:
            pass

    if g.user and g.user['timezone']:
        try:
            pytz.timezone(g.user['timezone'])
            return g.user['timezone']
        except pytz.UnknownTimeZoneError:
            pass

    return 'UTC'


@app.before_request
def before_request():
    """
    Executed before all other functions,
    sets the logged-in user in flask.g
    """
    user_id = request.args.get('login_as')
    if user_id:
        user = get_user(int(user_id))
        g.user = user
    else:
        g.user = None


@app.route('/', strict_slashes=False)
def index():
    """ Serves index page with parametrized templates """
    return render_template('7-index.html', title=_('home_title'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000', debug=True)
