from django.shortcuts import render
from .models import Contact, News, Sr, Say, Awards, RewardsCategories, NewsCategories, SrCategories
    

# Create your views here.
def index(request):
    say = Say.objects.all()
    news = News.objects.all()
    sr = Sr.objects.all()
    awards = Awards.objects.all()
    award = awards.first()
    return render(request, 'pages/index.html',{"award":award, "srs":sr, "news":news, "says":say, "title":""})

def about(request):
    say = Say.objects.all()
    return render(request, 'pages/about.html',{"says":say, "title":"عن"})

def awards(request):
    awards = Awards.objects.all()
    return render(request, 'pages/awards.html', {"awards":awards, "title":"الجوائز"})

def awardsdetails(request, id):
    award = Awards.objects.get(id=id)
    awards = Awards.objects.all()
    cat = RewardsCategories.objects.all()
    return render(request, 'pages/awardsdetails.html',{"awards":awards, "award":award, "categories":cat, "title":"الجوائز"})   

def contact(request):
    if request.method == 'POST':
        con =  Contact(
            nickname = request.POST.get('nickname'),
            name = request.POST.get('firstname'),
            email = request.POST.get('email'),
            address = request.POST.get('address'),
            phonenumber = request.POST.get('phonenumber'),
            subjct = request.POST.get('subjct'),
            whatq = request.POST.get('whatq'),
            what = request.POST.get('what'),
            message = request.POST.get('message'),
        )
        con.save()
    return render(request, 'pages/contact.html', {"title":"تواصل معي"})

def socialResponsibility(request):
    srs = Sr.objects.all()
    return render(request, 'pages/sr.html',{"srs":srs, "title":"المسؤلية الاجتماعية"}) 

def mediaandnews(request):
    news = News.objects.all()
    return render(request, 'pages/mediaandnews.html',{"news":news, "title":"الميديا والاخبار"})

def srdetails(request, id):
    news = News.objects.all()
    sr = Sr.objects.get(id=id)
    srs = Sr.objects.all()
    cat = SrCategories.objects.all()
    return render(request, 'pages/srdetails.html',{"news":news, "categories":cat, "sr":sr, "srs":srs, "title":"المسؤلية الاجتماعية"}) 

def newsdetails(request, id):
    new = News.objects.get(id=id)
    cat = NewsCategories.objects.all()
    news = News.objects.all()
    return render(request, 'pages/newsdetails.html',{"news":news, "new":new, "categories":cat, "title":"الاخبار"}) 
