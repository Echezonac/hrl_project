from django.shortcuts import render
from .models import *
from django.core.paginator import Paginator


# Create your views here.

def home(request):
    blog_list = Blog.objects.all().order_by('-id')
    paginator = Paginator(blog_list,3)
    page = request.GET.get('page')
    blog_list = paginator.get_page(page)
    context = {
     'Blogs': blog_list,   
    }
    return render(request, 'pages/index.html',context)

def detail_view(request,id):
    blog = Blog.objects.get(id=id)
    context = {
        'blog':blog
    }
    return render(request,'pages/blog_detail.html',context)


def services(request):
    return render(request, 'pages/services.html',{})

def offers(request):
    return render(request, 'pages/offers.html',{})

def contact(request):
    return render(request, 'pages/contact.html',{})

def booking(request):
    return render(request, 'pages/booking.html',{})

def dashboard(request):
    return render(request, 'pages/dashboard.html')
