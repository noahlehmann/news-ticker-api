from model.news_category import NewsCategory


class ArticleTagger:

    @staticmethod
    def tag_article(article):
        return [NewsCategory.OTHER]
