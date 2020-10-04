from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('projects/', views.projects, name="projects"),
	path('projects/<int:proj_id>', views.viewproject, name="viewproject"),
	path('features/', views.features, name="features"),
	path('contact/', views.contact, name="contact"),
]