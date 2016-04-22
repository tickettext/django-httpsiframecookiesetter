from django.conf.urls import url
from .views import cookiesetter

urlpatterns = [
    url(r'$', cookiesetter, name='cookiesetter'),
]
