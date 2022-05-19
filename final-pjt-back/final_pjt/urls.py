from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movies.urls')),
    path('accounts/', include('accounts.urls')),
    path('community/', include('articles.urls')),
]
