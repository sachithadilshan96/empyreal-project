from django.urls import path

from . import views

urlpatterns = [
    path('', views.services, name='services'),

    path('mortgage', views.mortgage, name='mortgage'),
    path('mortgagelist', views.index, name='mortgages'),
    path('mortgagelist/<int:mortgage_id>', views.mortgages, name='mortgagepage'),


    path('legal', views.legal, name='legal'),
    path('legallist', views.index_2, name='legals'),
    path('legallist/<int:legal_id>', views.legals, name='legalpage'),

    path('builder', views.builder, name='builder'),
    path('builderlist', views.index_3, name='builders'),
    path('builderlist/<int:builder_id>', views.builders, name='builderpage'),


    path('predict', views.predict, name='predict'),
    path('result', views.predict_results, name='result'),



]
