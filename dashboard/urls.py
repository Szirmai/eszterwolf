from django.urls import path
from .import views
from django.conf.urls import handler404, handler500

handler404 = 'dashboard.views.handler404'
handler500 = 'dashboard.views.handler500'

urlpatterns = [
    path('', views.home, name='dash-home'),
    path('login', views.logindash, name='login'),
    path('logout', views.logoutdash, name='logout'),
    
    path('category', views.category, name='category'),
    path('delete-category/mapping/<str:pk>', views.deleteCategoryMapping, name='delete-mapping-category'),
    path('delete-category/connectiong/<str:pk>', views.deleteCategoryConnecting, name='delete-connecting-category'),
    path('delete-category/painting/<str:pk>', views.deleteCategoryPainting, name='delete-painting-category'),
    path('uploads/categories/mapping', views.uploadCategoryMapping, name='upload-mapping-category'),
    path('uploads/categories/connecting', views.uploadCategoryConnecting, name='upload-connecting-category'),
    path('uploads/categories/painting', views.uploadCategoryPainting, name='upload-painting-category'),
    path('uploads/category', views.uploadCategories, name='upload-category'),
    
    path('painting', views.painting, name='painting'),
    path('delete-painting/<str:pk>', views.deletePainting, name='delete-painting'),
    path('update/painting/<str:pk>', views.updatePainting, name='update-painting'),
    path('uploads/paintings', views.uploadPainting, name='upload-painting'),
    
    path('mapping', views.mapping, name='mapping'),
    path('delete-mapping/<str:pk>', views.deleteMapping, name='delete-mapping'),
    path('update/mapping/<str:pk>', views.updateMapping, name='update-mapping'),
    path('uplaods/mapping', views.uploadMapping, name='upload-mapping'),
    
    path('connecting', views.connecting, name='connecting'),
    path('delete-connecting/<str:pk>', views.deleteConnecting, name='delete-connecting'),
    path('update/connecting/<str:pk>', views.updateConnecting, name='update-connecting'),
    path('uploads/connecting', views.uploadConnecting, name='upload-connecting'),

]