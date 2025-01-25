from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('lessons/eng', views.EnglishLessons.as_view(), name='eng'),
    path('lessons/hist', views.HistoryLessons.as_view(), name='hist'),
    path('lessons/psych', views.PsychologyLessons.as_view(), name='psych'),
    ]