from . import views
from django.urls import path



urlpatterns = [
    path('home/',views.home,name="home"),
    path('new_post/',views.new_post,name="new_post"),
    path('view_all/',views.view_all,name="view_all"),
    path('search/',views.search,name="search"),
]