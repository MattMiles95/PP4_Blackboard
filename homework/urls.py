from django.urls import path
from . import views


urlpatterns = [
    path('', views.homework_submission, name='homework'),
    path('ajax/load-lessons/', views.load_lessons, name='ajax_load_lessons'), # AJAX
]