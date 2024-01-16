from django.urls import path

from service.apply_logic import check_application, toggle_application
from service.favorites_logic import add_or_remove_favorite, check_favorite_status
from service.views import feed, search

app_name = 'service'

urlpatterns = [
    path('', feed, name='feed'),

    path('search/', search, name='search'),

    path('toggle_application/<int:pk>/', toggle_application, name='toggle_application'),

    path('check_application/<int:pk>/',
         check_application,
         name='check_application'),

    path('favorite/<str:type>/<int:pk>/', add_or_remove_favorite,
         name='toggle-favorite'),

    path('favorite/status/<str:type>/<int:pk>/', check_favorite_status,
         name='check-favorite-status'),
]
