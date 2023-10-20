from django.urls import path

from . import views

urlpatterns = [
    path('new-register/', views.new_register, name='new-register'),
    path('add-report/', views.add_report, name='add-report'),
    path('reports/details/<int:id>', views.details),
    path('reports/delete/<int:id>', views.delete),
    path('reports/finish/<int:id>', views.finish)
]
