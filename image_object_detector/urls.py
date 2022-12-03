from django.urls import path

from . import views

urlpatterns = [
  path('', views.IndexView.as_view(), name = 'index'),
  path('show/', views.ShowView.as_view(), name = 'show'),
]
