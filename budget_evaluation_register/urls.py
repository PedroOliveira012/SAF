from django.urls import path

from . import views

urlpatterns = [
    path('new-register/', views.new_register, name='new-register'),
    # path('reports/', views.reports),
]
