from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name="home"),
    path('about/', views.about,name="about"),
    path('delete/<list_id>', views.delete, name='delete'),
    path('edit/<list_id>', views.edit, name='edit'),

]