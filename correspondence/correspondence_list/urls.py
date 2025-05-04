from django.urls import path
from . import views

app_name='correspondence_list'

urlpatterns = [    
    path('', views.home, name='home'),
    path('create/', views.create_correspondence, name='create'),
    path('<slug>/', views.correspondence_detail, name='detail'),
    path('<slug>/update/', views.update_correspondence, name='update_correspondence'),
]
