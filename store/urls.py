from django.conf.urls import url

from store import views
from store.views import store

urlpatterns=[
    url(r'', store, name='index'),
]
