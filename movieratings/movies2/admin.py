from django.contrib import admin
from movies2.models import Movie, Rating, Rater


# Register your models here.
@admin.register(Movie)
class MoviesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre')


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('get_rater_id',  'movie', 'rating', 'timestamp')


@admin.register(Rater)
class rater(admin.ModelAdmin):
    list_display = ('gender',  'age', 'occupation')




