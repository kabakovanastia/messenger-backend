from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_msg, name='add-msg'),
    path('all/', views.view_msgs, name='view-msgs'),
]
