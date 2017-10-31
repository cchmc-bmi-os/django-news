from django.utils.feedgenerator import Atom1Feed, Rss201rev2Feed, \
    RssUserland091Feed
from django.contrib.syndication.views import Feed
from models import Article


class LatestArticles(Feed):
    title = ''
    link = ''
    author_link = ''
    description = ''
    copyright = ''
    author_name = ''
    author_email = ''
    description = ''
    ttl = '1'

    title_template = 'feeds/news/article_title.html'
    description_template = 'feeds/news/article_description.html'

    def item_author_name(self, obj):
        if obj.author:
            return obj.author.get_full_name()
        return None

    def item_author_email(self, obj):
        if obj.author:
            return obj.author.email

        return None

    def item_pubdate(self, obj):
        return obj.created

    def item_link(self, obj):
        return obj.get_absolute_url()

    def items(self):
        return Article.objects.all().filter(published=True).order_by('-created')[:15]


class RSSv1LatestArticles(LatestArticles):
    link = "/rss/v1/"
    feed_type = RssUserland091Feed


class RSSv2LatestArticles(LatestArticles):
    link = "/rss/v2/"
    feed_type = Rss201rev2Feed


class AtomLatestArticles(LatestArticles):
    link = "/atom/v1/"
    subtitle = LatestArticles.description
    feed_type = Atom1Feed
