from django.urls import path
from .views import show_about_page, show_home_page,show_category_page

urlpatterns =[
  path('about/',show_about_page,name='about'),
  path('',show_home_page,name='home'),
  path('category/<int:cid>/',show_category_page),
]