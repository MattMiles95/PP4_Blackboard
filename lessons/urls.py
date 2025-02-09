from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('lessons/eng', views.EnglishLessons.as_view(), name='eng'),
    path('lessons/hist', views.HistoryLessons.as_view(), name='hist'),
    path('lessons/psych', views.PsychologyLessons.as_view(), name='psych'),
    path('<slug:slug>/', views.lesson_detail, name='lesson_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>/', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>/', views.comment_delete, name='comment_delete'),
    path('<slug:slug>/report_comment/<int:comment_id>/', views.comment_report, name='comment_report'),
    ]
