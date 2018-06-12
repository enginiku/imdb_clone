from django.urls import path

from . import views

urlpatterns = [
	path('list', views.index, name='index'),
	path('create', views.create, name='create'),
	path('<int:id>/edit', views.edit, name='edit'),
	path('<int:id>/update', views.update, name='update'),
	path('<int:id>/delete', views.delete, name='delete'),
	path('search', views.search, name='search')
]