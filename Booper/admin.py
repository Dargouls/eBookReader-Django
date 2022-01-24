from django.contrib import admin
from .models import Arquivo, Post, SiteUser
# Register your models here.

admin.site.register(Post)

admin.site.register(Arquivo)

@admin.register(SiteUser)
class SiteAdmin(admin.ModelAdmin):
  list_display = ('username', 'email')
  search_fields = ('username', 'email')
  prepopulated_fields = {'slug':['username'],}