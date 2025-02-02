from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('homework/', include('homework.urls'), name='homework-urls'),
    path('summernote/', include('django_summernote.urls')),
    path('', include('lessons.urls'), name='lessons-urls'),
]