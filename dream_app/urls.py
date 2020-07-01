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
    path('videos', views.media_videos, name ='media-videos'),
    path('photos', views.media_photos, name ='media-photos'),
    path('camps', views.camp, name ='camp_list'),
    path('camps/<int:id>/', views.camp_detail, name ='camp_detail'),
]