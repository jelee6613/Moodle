from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    movies = models.ManyToManyField('movies.Movie', through='movies.WatchedMovie', related_name='users')
    followings = models.ManyToManyField('self', related_name='followers', symmetrical=False)
