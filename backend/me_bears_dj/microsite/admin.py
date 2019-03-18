from django.contrib import admin
from .models import Page, Section, Content
# Register your models here.


class PageAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Page, PageAdmin)
admin.site.register(Section)
admin.site.register(Content)
