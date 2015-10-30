from django.contrib.auth.models import User
from django.db import models
from django import forms
from django.db.models import Avg
import users
from users.models import Profile


class Movie(models.Model):
    title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)

    @property
    def average_rating(self):
        avg = 0
        ratings = self.rating_set.all()
        for rating in ratings:
            avg += rating.rating
        return avg

    def __str__(self):
        return "title: {}, genre: {}".format(self.title, self.genre)


class Rater(models.Model):
    gender = models.CharField(max_length=20)
    age = models.IntegerField()
    occupation = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    user = models.OneToOneField(Profile)

    #def rate_movie:

    def __str__(self):
        return "rater: {}, movie{}, rating{}, timestamp: {}".format(self.gender,
                                                                    self.age,
                                                                    self.occupation,
                                                                    self.zip_code)


class Rating(models.Model):
    rater = models.ForeignKey(Rater)
    movie = models.ForeignKey(Movie)
    rating = models.IntegerField()
    timestamp = models.CharField(max_length=200)


    def __str__(self):
        return "rater: {}, movie: {}, rating: {}, timestamp: {}".format(self.rater.id,
                                                                    self.movie.title,
                                                                    self.rating,
                                                                    self.timestamp)
    def get_rater_id(self):
        return self.rater.id
    get_rater_id.short_description = 'Rater Id'