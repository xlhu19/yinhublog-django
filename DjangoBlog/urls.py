from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from DjangoBlog.sitemap import StaticViewSitemap, ArticleSiteMap, CategorySiteMap, TagSiteMap, UserSiteMap
from DjangoBlog.feeds import DjangoBlogFeed
from django.views.decorators.cache import cache_page
from django.conf import settings
from django.conf.urls.static import static

sitemaps = {

    'blog': ArticleSiteMap,
    'Category': CategorySiteMap,
    'Tag': TagSiteMap,
    'User': UserSiteMap,
    'static': StaticViewSitemap
}

handler404 = 'blog.views.page_not_found_view'
handler500 = 'blog.views.server_error_view'

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'', include('blog.urls', namespace='blog', app_name='blog')),
                  url(r'', include('comments.urls', namespace='comment', app_name='comments')),
                  url(r'', include('accounts.urls', namespace='account', app_name='accounts')),
                  url(r'', include('oauth.urls', namespace='oauth', app_name='oauth')),
                  url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
                  url(r'^feed/$', DjangoBlogFeed()),
                  url(r'^search', include('haystack.urls'), name='search'),
                  url(r'', include('servermanager.urls', namespace='servermanager', app_name='servermanagers'))
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

