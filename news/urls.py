from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^news/(?P<news>[0-9]+)/$', views.news, name='news_1'),
]