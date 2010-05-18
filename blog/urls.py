from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    url(r'^$', 'posts', name='posts'),
    url(r'^js$', 'test_js'),
)
