from django.conf.urls import url
from movies2.views import list_all_movies, MovieDetail, RaterDetail
from . import views

urlpatterns = (
    url(r'^$', views.list_all_movies, name='list_movies'),
    url(r'^(?P<pk>\d+)/$', MovieDetail.as_view(), name='movie_detail'),
    url(r'^rater/(?P<pk>\d+)/$', RaterDetail.as_view(), name='rater_detail'),
)
