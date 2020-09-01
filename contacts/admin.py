from django.contrib import admin

from .models import Contact
from .models import Comment,CommentBuilder
from services.models import Mortgage

class ContactAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'listing', 'email', 'contact_date')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'email', 'listing')
  list_per_page = 25

admin.site.register(Contact, ContactAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('mortgage_id','created', 'active')
    list_filter = ('mortgage_id','created')
    search_fields = ('mortgage_id', 'active')

admin.site.register(Comment, CommentAdmin)


class CommentBuilderAdmin(admin.ModelAdmin):
    list_display = ('builder_id','created', 'active')
    list_filter = ('builder_id','created')
    search_fields = ('builder_id', 'active')

admin.site.register(CommentBuilder, CommentBuilderAdmin)
