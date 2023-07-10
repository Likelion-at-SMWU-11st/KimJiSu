from django.contrib import admin
from django.urls import path

from posts.views import url_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('url/', url_view),
]
