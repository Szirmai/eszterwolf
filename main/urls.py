from django.urls import path
from .import views
from django.conf.urls import handler404, handler500

handler404 = 'main.views.handler404'
handler500 = 'main.views.handler500'

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('cv', views.cv, name='cv'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('connecting', views.connectingTopic, name='connecting-topic'),
    path('connecting/subtopic/<str:pk>', views.connectingSubTopic, name='connecting-subtopic'),
    path('connecting/<str:pk>', views.connectingCertain, name='connecting-certain'),
    path('contact', views.contact, name='contact'),
    path('info', views.info, name='info'),
    path('mapping', views.mappingTopic, name='mapping-topic'),
    path('mapping/subtopic/<str:pk>', views.mappingSubTopic, name='mappings-sub-topic'),
    path('mapping/<str:pk>', views.mappingCertain, name='mapping-certain'),
    path('paintings', views.paintingTopic, name='painting-topic'),
    path('paintings/subtopic/<str:pk>', views.paintingSubTopic, name='paintings-sub-topic'),
    path('paintings/<str:pk>', views.paintingCertain, name='painting-certain'),
]
