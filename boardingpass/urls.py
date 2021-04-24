from django.urls import path

from . import views, mqtt

urlpatterns = [
	path('', views.index, name='index'),
	path('<int:kode>', views.pantau, name='pantau'),
]