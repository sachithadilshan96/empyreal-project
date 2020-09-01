from django.contrib import admin

from .models import Mortgage,Legal,Builder



class MortgageAdmin(admin.ModelAdmin):
  list_display = ('id', 'title','user','city', 'zipcode')
  list_display_links = ('id', 'title')
  list_filter = ('zipcode',)
  search_fields = ('user', 'title', 'zipcode')

admin.site.register(Mortgage, MortgageAdmin)

class LegalAdmin(admin.ModelAdmin):
  list_display = ('id', 'title','user','city', 'zipcode')
  list_display_links = ('id', 'title')
  list_filter = ('zipcode',)
  search_fields = ('user', 'title', 'zipcode')

admin.site.register(Legal, LegalAdmin)


class BuilderAdmin(admin.ModelAdmin):
  list_display = ('id', 'company_name','user','city', 'zipcode')
  list_display_links = ('id', 'user')
  list_filter = ('zipcode',)
  search_fields = ('user', 'title', 'zipcode')

admin.site.register(Builder, BuilderAdmin)
