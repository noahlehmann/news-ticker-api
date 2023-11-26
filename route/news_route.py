from flask import Blueprint, Response

from model.news_category import NewsCategory
from model.response_model import ResponseModel
from service.nytimes_rss_service import NyTimesRssService

news_api = Blueprint("news_api", __name__)


@news_api.route('/news')
def news() -> Response:
    articles = NyTimesRssService().get_articles()
    return ResponseModel(articles).build()


@news_api.route('/news/tags')
def tags() -> Response:
    return ResponseModel([category.value for category in NewsCategory]).build()


