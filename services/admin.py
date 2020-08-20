from django.contrib import admin

from .models import Mortgage

class MortgageAdmin(admin.ModelAdmin):
  list_display = ('id', 'title','user','city', 'zipcode')
  list_display_links = ('id', 'title')
  list_filter = ('zipcode',)
  search_fields = ('user', 'title', 'zipcode')

admin.site.register(Mortgage, MortgageAdmin)
