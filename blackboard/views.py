from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError

def custom_404_view(request, exception):
    return render(request, 'errors/404.html', status=404)

def custom_500_view(request):
    return render(request, 'errors/500.html', status=500)