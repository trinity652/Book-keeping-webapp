from . import views
from django.urls import path, include,re_path
app_name = 'queryapp'

urlpatterns = [
	path('mainpage/', views.MainPage),
]