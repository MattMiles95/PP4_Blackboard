from django.contrib import admin
from django.urls import path, include
from django.views.defaults import page_not_found, server_error
from .views import custom_404_view, custom_500_view

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('homework/', include('homework.urls'), name='homework-urls'),
    path('summernote/', include('django_summernote.urls')),
    path('', include('lessons.urls'), name='lessons-urls'),
]

handler404 = 'blackboard.views.custom_404_view'
handler500 = 'blackboard.views.custom_500_view'
