from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('add_watched_movie/', views.add_watched_movie, name='add_watched_movie'),
    path('watched_movies/', views.watched_movies, name='watched_movies'),
    path('api/most_watched_movies/', views.most_watched_movies, name='most_watched_movies_api'),
]

""" #from django.conf.urls import url
from api import views
from django.urls import re_path as url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^test$', views.testApi),
    url(r'^test/([0-9]+)$', views.testApi),
    url(r'^test/savefile', views.SaveFile),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 """