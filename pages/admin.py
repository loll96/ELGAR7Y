from django.contrib import admin
from .models import Contact, News, Sr, Say, Awards, Source, RewardsCategories, NewsCategories, SrCategories
# Register your models here.

admin.site.register(Contact)
admin.site.register(News)
admin.site.register(Sr)
admin.site.register(Say)
admin.site.register(Awards)
admin.site.register(Source)
admin.site.register(RewardsCategories)
admin.site.register(NewsCategories)
admin.site.register(SrCategories)

