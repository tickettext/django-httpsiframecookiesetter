from django.conf.urls import patterns, url
from .views import cookiesetter

urlpatterns = [
    url(r'$', cookiesetter, name='cookiesetter'),
]
