from django.db import models
from django.conf import settings


User = settings.AUTH_USER_MODEL

class Movie(models.Model):
    title = models.CharField(max_length=50)
    genre = models.CharField(max_length=30)
    overview = models.TextField()
    poster_path = models.TextField()
    backdrop_path = models.TextField()
    director = models.CharField(max_length=30)
    average_vote = models.FloatField(default=0.0)
    release_date = models.DateField(null=True)

    def __str__(self):
        return f'{self.title} : {self.director}'


class WatchedMovie(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    rate = models.FloatField(default=0.0)


class Question(models.Model):
    content = models.CharField(max_length=100)

    def __str__(self):
        return self.content


class Value(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    director = models.CharField(max_length=30, null=True)
