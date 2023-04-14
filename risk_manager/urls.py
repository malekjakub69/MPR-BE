# task.urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('random/<str:pk>/', views.random, name='random'),
    path('user/<str:pk>/', views.get_user, name='user'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('users', views.get_users, name='get_users'),
    path('projects', views.get_projects, name='get_projects'),
    path('project/<str:pk>', views.get_project, name='get_project'),
    path('risks/<str:pk>', views.get_risks, name='get_risks'),
    path('risk/<str:pk>', views.get_risk, name='get_risk'),
    path('get_project/<str:pk>', views.get_project, name='get_project'),
    path('create_project', views.create_project, name='create_project'),
    path('create_risk', views.create_risk, name='create_risk'),
    path('update_risk', views.update_risk, name='update_risk'),
    path('update_project', views.update_project, name='update_project')
]
