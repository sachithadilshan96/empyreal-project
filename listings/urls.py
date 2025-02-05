from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
    path('like/<int:pk>', views.like, name='like_listing'),
    path('map/<int:listing_id>', views.map, name='map'),
    path('avmap/<int:listing_id>', views.avmap, name='avmap'),

]
