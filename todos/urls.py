from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('<int:id>/', views.detail, name='detail'),
    path('<int:id>/edit', views.edit, name='edit'),
]
