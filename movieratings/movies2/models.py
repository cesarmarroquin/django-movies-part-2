from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.db.models import Avg
import users






class Rater(models.Model):
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    occupation = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    user = models.OneToOneField(User, null=True)

    #def rate_movie:

    def __str__(self):
        return "rater: {}, movie{}, rating{}, timestamp: {}".format(self.gender,
                                                                    self.age,
                                                                    self.occupation,
                                                                    self.zip_code)

class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)

    def all_ratings(self):
        return self.rating_set.all()

    @property
    def average_rating(self):
        movie = self.rating_set.all().aggregate(Avg("rating"))["rating__avg"]
        return movie

    @property
    def all_raters(self):
        raters = self.rating_set.all().filter()
        return raters

    def __str__(self):
        return "title: {}, genre: {}".format(self.title, self.genre)




class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField()
    timestamp = models.CharField(max_length=200)
    #user = self.rater_set.user

    @property
    def all_raters(self):
        raters = self.rater_set.all()
        return raters

    def __str__(self):
        return "rater: {}, movie: {}, rating: {}, timestamp: {}".format(self.rater.id,
                                                                    self.movie.title,
                                                                    self.rating,
                                                                    self.timestamp)
    def get_rater_id(self):
        return self.rater.id
    get_rater_id.short_description = 'Rater Id'


