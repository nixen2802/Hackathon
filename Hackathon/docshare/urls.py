from django.urls import path,include
from . import views
from users import views as user_views
urlpatterns = [
    path('', views.home, name="Home page"),
    path('about/',views.about,name="About page"),
    path('register/', user_views.register),
]
