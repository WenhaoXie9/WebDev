from ProjectView import views
from django.urls import re_path as url
urlpatterns = [
    url(r'^project$',views.projectApi),
    url(r'^project/([0-9]+)',views.projectApi)
]