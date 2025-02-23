from django.contrib import admin
from .models import Contact, Management, Permission

class ContactAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'position', 'status', 'management', 'district')
    search_fields = ('full_name', 'phone_number', 'position')
    list_filter = ('status', 'district', 'management')
    class Media:
        js = [
            "admin/js/jquery.init.js",  # Django admin jQuery
            "admin/js/filter_management.js",
        ]

admin.site.register(Contact, ContactAdmin)
admin.site.register(Management)
admin.site.register(Permission)