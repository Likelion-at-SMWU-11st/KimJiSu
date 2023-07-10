from django.contrib import admin
from django.urls import path

from posts.views import url_view
from posts.views import url_parameter_view
from posts.views import function_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('url/', url_view),
    path('url/<int:username>/', url_parameter_view),
    path('fbv/', function_view),
]