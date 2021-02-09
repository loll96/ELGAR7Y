from django.urls import path
from . import views

app_name = 'garhy'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('awards/', views.awards, name='awards'),
    path('awardsdetails/<int:id>', views.awardsdetails, name='awardsdetails'),
    path('contact/', views.contact, name='contact'),
    path('socialResponsibility/', views.socialResponsibility, name='socialResponsibility'),
    path('mediaandnews/', views.mediaandnews, name='mediaandnews'),
    path('srdetails/<int:id>', views.srdetails, name='srdetails'),
    path('newsdetails/<int:id>', views.newsdetails, name='newsdetails'),
]