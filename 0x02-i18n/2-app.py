#!/usr/bin/env python3
""" first flask app """
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

class Config(object):
    """ a class for configaration of babel """
    LANGUAGES =  ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

app.config.from_object(Config)

@babel.localeselector
def get_locale():
    """ return the best match from the Accept-Language header """
    return request.accept_languages.best_match(app.config["LANGUAGES"])

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Prints a Message when / is called """
    return render_template('0-index.html')