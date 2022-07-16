from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('update', views.update_task),
    path('<int:id>/', views.describe_task),
    path('<int:id>/edit', views.edit_task),
    path('new', views.signup_form)
]