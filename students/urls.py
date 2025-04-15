from django.contrib import admin
from django.urls import path
from studentsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listone/', views.listone, name='listone'),
    path('listall/', views.listall, name='listall'),
    path('', views.index, name='home'),
    path('index/', views.index, name='index'),
    path('init/', views.initdata, name='init'),  
]
