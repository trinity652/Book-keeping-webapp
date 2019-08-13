from . import views
from django.urls import path, include,re_path
app_name = 'app1'

urlpatterns = [
	path('mainpage/', views.MainPage),
	re_path(r'^mainpage/app1/results/(?P<BookName>.*)/$', views.ViewLookBook),
]