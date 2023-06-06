#!/usr/bin/env python3
""" Starts a Flask web application """
from flask import Flask, render_template, request
from flask_babel import Babel, gettext as _

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Language and locale configs """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """ Selects the best language based on user's preferences """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """ Serves index page with parametrized templates """
    return render_template('3-index.html',
                           title=_('home_title'),
                           header=_('home_header'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
