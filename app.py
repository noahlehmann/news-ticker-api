import os

from dotenv import load_dotenv
from flask import Flask

from route.news_route import news_api
from util.json_encoder import DictJSONEncoder

load_dotenv()


def create_app():
    app = Flask(__name__)

    app.register_blueprint(news_api)
    app.json_encoder = DictJSONEncoder

    app.config['API_VERSION'] = "0.0.1"

    app.config['RSS_US'] = os.getenv('RSS_US')

    return app


if __name__ == '__main__':
    create_app().run()
