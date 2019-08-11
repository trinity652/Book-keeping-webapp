from . import views
from django.urls import path, include,re_path
app_name = 'app1'

urlpatterns = [
	path('mainpage/', views.MainPage),
	path('bookname/<slug:BookName>', views.ViewLookBook),
]