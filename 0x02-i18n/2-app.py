#!/usr/bin/env python3
"""
This Modules initailizes the flask app 
"""
from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)


class Config(object):
    """
    This a config class
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


def get_locale() -> str:
    """
    This is used to make the choose the most preperred language
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel = Babel(app)
babel.init_app(app, locale_selector=get_locale)
app.config.from_object(Config)


@app.route("/")
def home() -> str:
    """
    handles the home route
    """
    return render_template("2-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
