#!/usr/bin/env python3
"""
This Modules initailizes the flask app 
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """
    This a config class
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """
    This is used to make the choose the most preperred language
    """
    preferred_locale = request.args.get('locale')
    if preferred_locale in app.config['LANGUAGES']:
        return preferred_locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def home() -> str:
    """
    handles the home route
    """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
