from django.contrib import admin
from .models import  UserProfile
#UserProfile class
class UserProfileAdmin(admin.ModelAdmin):
  list_display = ("user","city", "zipcode",)
  list_display_links = ("user",)
  list_filter = ("zipcode",)
  search_fields = ("user",)

admin.site.register(UserProfile, UserProfileAdmin)
