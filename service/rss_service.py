from abc import ABC, abstractmethod

import feedparser

from service.article_tagger import ArticleTagger


class RssParseService(ABC):
    def __init__(self, url):
        self._url = url
        self._feed = None
        self._articles = []

    def get_articles(self):
        if not self._articles:
            self._get_feed_for_today()
        return self._articles

    def _get_feed_for_today(self):
        if not self._feed:
            self._feed = feedparser.parse(self._url)
        self._articles = self._transform_feed_entries_to_article(self._feed)
        self._tag_news_articles()
        return self._feed

    @abstractmethod
    def _transform_feed_entries_to_article(self, feed):
        pass

    def _tag_news_articles(self):
        for article in self._articles:
            if not article.tags:
                article.tags = ArticleTagger.tag_article(article)

    @abstractmethod
    def _get_headline_from_entry(self, entry):
        pass

    @abstractmethod
    def _get_summary_from_entry(self, entry):
        pass

    @abstractmethod
    def _get_link_from_entry(self, entry):
        pass



