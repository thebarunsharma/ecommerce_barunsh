from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

def index(request):
    return render(request, 'index.html',{})
def about(request):
    return render(request, 'about.html', {})
def destination(request):
    return render(request, 'travel_destination.html', {})
def blog(request):
    return render(request, 'blog.html', {})
def singleblog(request):
    return render(request, 'single-blog.html', {})