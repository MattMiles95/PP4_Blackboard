from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeworkDashboardView.as_view(), name='homework_dashboard'),
    path('submission/<str:subject>/', views.HomeworkSubmissionView.as_view(), name='homework_submission'),
]