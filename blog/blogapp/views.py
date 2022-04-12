from unicodedata import category
from django.shortcuts import render
from django.template import RequestContext
from .forms import *


# Create your views here.

def home(request):
    return render(request,'home.html')


def new_post(request):
        context ={}
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save() 
        context['form']= form
        return render(request, "create_post.html", context)

def view_all(request):
        blog = Blog.objects.all()
        category = Category.objects.all()
        return render(request,'view_all_post.html', {'blog':blog,'category':category})   


def search(request):
    id = request.GET['dropdown'] 
    category = Category.objects.all()
    if id == '0':
        blog = Blog.objects.all()
    else:    
        blog = Blog.objects.filter(id=id)
    return render(request,'view_all_post.html', {'blog':blog,'category':category})   
