from django.urls import path

from . import views

app_name = 'app'

urlpatterns = [
	path('', views.index, name='index'),
	path('register', views.register, name='register'),
	path('login', views.login, name='login'),
	path('incident', views.incident, name='incident'),
	path('incidentprocess', views.incidentprocess, name='incidentprocess'),
	path('logout', views.logout, name='logout')

]