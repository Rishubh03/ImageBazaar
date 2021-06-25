from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Category, Images
# Create your views here.

def show_about_page(request):
  link="www.google.com"
  name="Rishubh Kumar"
  data={
    'link':link,
    'name':name

  }
  return render(request,'about.html',data)

def show_home_page(request):
    images=Images.objects.all()
    cats=Category.objects.all()
    data={
      'images':images,
      'cats':cats
    }
    return render(request,'home.html',data)

def show_category_page(request,cid):
    cats=Category.objects.all()
    cat=Category.objects.get(pk=cid)
    images=Images.objects.filter(cat=cat)
    data={
      'images':images,
      'cats':cats
    }
    return render(request,'home.html',data)