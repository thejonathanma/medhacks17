from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create_account/', views.create_account, name='create_account'),
    url(r'^create_profile/', views.create_profile, name='create_profile')
]
