from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ['Fullname','Phone','is_read_admin']
    list_editable = ['is_read_admin']
    list_filter = ['is_read_admin']

admin.site.register(Contact,ContactAdmin)