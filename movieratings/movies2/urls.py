from django.conf.urls import url

urlpatterns = (
    url(r'^$', 'movies2.views.list_movies', name='list_movies'),
)
