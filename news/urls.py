from django.conf.urls.defaults import url, patterns
from feeds import RSSv1LatestArticles, RSSv2LatestArticles, AtomLatestArticles, LatestArticles
from views import ArticleDetailView


urlpatterns = patterns('',
    url(r'^$', LatestArticles(), name='news_index'),

    url(r'^article/edit/$', 'news.views.edit_article', name='news_article_edit'),
    url(r'^article/edit/(?P<article_id>[\d]+)/$', 'news.views.edit_article', name='news_article_edit'),
    url(r'^article/delete/(?P<article_id>[\d]+)/$', 'news.views.delete_article', name='news_article_delete'),
    url(r'^article/(?P<pk>[\d]+)/$', ArticleDetailView.as_view(), name='news_article'),
    url(r'^article/(?P<slug>[^/]+)/$', ArticleDetailView.as_view(), name='news_article'),

    url(r'^rss/v1/$', RSSv1LatestArticles(), name='news_feed_rss'),
    url(r'^rss/v2/$', RSSv2LatestArticles(), name='news_feed_rss2'),
    url(r'^atom/v1/$', AtomLatestArticles(), name='news_feed_atom'),
)

