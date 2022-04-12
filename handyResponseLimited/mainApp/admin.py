from django.contrib import admin
from . models import Blog

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display =['title' , 'date']
    list_display_links = ['title' , 'date']

admin.site.register(Blog, BlogAdmin)

