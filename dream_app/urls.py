from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='homepage'),
    path('about', views.about, name ='about'),
    path('shop', views.shop, name ='shop'),
    path('events', views.events, name ='events'),
    path('team', views.team, name ='team'),
    path('contact-page', views.contact, name ='contact-page'),
    path('careers', views.jobs, name ='careers'),
    path('process', views.process_contact, name ='process'),
    path('sponsors', views.sponsors, name ='sponsors'),
    path('founders', views.founder, name ='founders'),
    path('dreamsmedia', views.media, name ='dreamsmedia'),
    path('dreamsmedia/photos', views.media, name ='media-photos'),
    path('hdreams-camp', views.camp, name ='camp'),
]