#!/usr/bin/env python3
"""
A Basic flask application
"""
from flask_babel import Babel
from flask import Flask, render_template, request


class Config(object):
    """
    Application configuration class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


# Instantiate the application object
app = Flask(__name__)
app.config.from_object(Config)

# Wrap the application with Babel
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """
    Gets locale from request object
    """
    locale = request.args.get('locale', '').strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Renders a basic html template
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
