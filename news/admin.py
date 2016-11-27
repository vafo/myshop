from django.contrib import admin

from news.models import News


class NewsAdmin(admin.ModelAdmin):
    exclude = ['posted']

admin.site.register(News, NewsAdmin)
