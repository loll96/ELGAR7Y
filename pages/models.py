from django.db import models
from datetime import datetime

class Contact(models.Model):
    choice1 = [
        ('اقتصادي','اقتصادي'),
        ('سياسي','سياسي'),
        ('رياضي','رياضي'),
        ('تواصل','تواصل'),
    ]
    choice2 = [
        ('استثمارات','استثمارات'),
        ('انشاءات','انشاءات'),
        ('تنمية وتطوير','تنمية وتطوير'),
        ('غير ذلك','غير ذلك'),
    ]

    nickname = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=20)
    subjct = models.CharField(max_length=100)
    whatq = models.CharField(max_length=100,  choices=choice1)
    what = models.CharField(max_length=100,  choices=choice2)
    message = models.TextField()

    def __str__(self):
        return self.subjct

class NewsCategories(models.Model):
    title = models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
        return self.title

class Source(models.Model):
    name = models.CharField(max_length=100,null=True, blank=True)
    link = models.CharField(max_length=250,null=True, blank=True)
    def __str__(self):
        return self.name

class News(models.Model):
    img = models.ImageField(upload_to = 'images/News', null=True, blank=True)
    title = models.CharField(max_length=200)
    time = models.DateTimeField(default=datetime.now)
    content = models.TextField()
    bigcontent = models.TextField()
    category = models.ForeignKey(NewsCategories, on_delete=models.CASCADE)
    sources = models.ManyToManyField(Source)

    def __str__(self):
        return self.title
class SrCategories(models.Model):
    title = models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
        return self.title

class Sr(models.Model):
    title = models.CharField(max_length=200)
    time = models.DateTimeField(default=datetime.now)
    img = models.ImageField(upload_to = 'images/sr', null=True, blank=True)
    content = models.TextField()
    category = models.ForeignKey(SrCategories, on_delete=models.CASCADE)
    sources = models.ManyToManyField(Source)
    
    def __str__(self):
        return self.title

class Say(models.Model):
    img = models.ImageField(upload_to = 'images/say', null=True, blank=True)
    name = models.CharField(max_length=100)
    content = models.TextField()
    job = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RewardsCategories(models.Model):
    title = models.CharField(max_length=100,null=True, blank=True)
    def __str__(self):
        return self.title
   
class Awards(models.Model):
    img = models.ImageField(upload_to = 'images/awards', null=True, blank=True)
    title = models.CharField(max_length=100)
    time = models.DateTimeField(default=datetime.now)
    content = models.TextField()
    bigcontent = models.TextField()
    df = models.TextField()
    sources = models.ManyToManyField(Source)
    category = models.ForeignKey(RewardsCategories, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    



