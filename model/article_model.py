from model.serializable import Serializable


class ArticleModel(Serializable):
    def __init__(self, headline, summary, link, tags=None):
        self.headline = headline
        self.summary = summary
        self.link = link
        self.tags = tags if tags else []

    def to_dict(self):
        return {
            "headline": str(self.headline),
            "summary": str(self.summary),
            "link": str(self.link),
            "tags": [str(tag.value) for tag in self.tags]
        }


