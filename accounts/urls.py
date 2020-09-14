from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboardxx', views.dashboard, name='dashboardx'),
    path('profile', views.profile, name='profile'),
    path('userprofile', views.userprofile, name='userprofile'),
    path('dashboard', views.userlistings, name='userlistings'),
    path('userlistings/<int:listing_id>/delete', views.deletelistings,name='deletelistings'),
    path('editlisting/<int:listing_id>/', views.editlistings,name='editlisting'),
    path('marketpredict', views.marketpredict, name='marketpredict'),
]
