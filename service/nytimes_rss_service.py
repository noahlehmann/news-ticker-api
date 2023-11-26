from flask import current_app

from model.article_model import ArticleModel
from service.rss_service import RssParseService


class NyTimesRssService(RssParseService):

    def __init__(self):
        super().__init__(current_app.config["RSS_US"])

    def _get_headline_from_entry(self, entry):
        return entry.get("title")

    def _get_summary_from_entry(self, entry):
        return entry.get("description")

    def _get_link_from_entry(self, entry):
        return entry.get("link")

    def _transform_feed_entries_to_article(self, feed):
        articles = []
        for entry in feed.entries:
            articles.append(ArticleModel(
                headline=self._get_headline_from_entry(entry),
                summary=self._get_summary_from_entry(entry),
                link=self._get_link_from_entry(entry)
            ))
        return articles

