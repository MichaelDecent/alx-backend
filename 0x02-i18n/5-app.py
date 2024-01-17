#!/usr/bin/env python3
"""
This Modules initailizes the flask app 
"""
from flask import Flask, render_template, request
from flask_babel import Babel
from typing import Union, Dict


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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """Retrieve a user from database if login_as is passed
    to the request URL and the ID can be found, else none"""

    user_id = request.args.get("login_as")
    if user_id:
        return users.get(int(user_id))
    return None


@app.before_request
def before_request() -> None:
    """Execute before all other function.
    Set output of the get_user method as global"""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """
    This is used to make the choose the most preperred language
    """
    preferred_locale = request.args.get("locale")
    if preferred_locale in app.config["LANGUAGES"]:
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
