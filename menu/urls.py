from django.urls import path
from . import views

app_name = 'menu' 

urlpatterns = [
    path('', views.menu_view, name='menu_view'),   
    path('switch_language/<str:language>/', views.switch_language, name='switch_language'),
]
