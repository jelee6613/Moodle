from django.contrib import admin
from .models import Movie, Question, Value, WatchedMovie

admin.site.register(Movie)
admin.site.register(Question)
admin.site.register(Value)
admin.site.register(WatchedMovie)