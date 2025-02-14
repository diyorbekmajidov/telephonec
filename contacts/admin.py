from django.contrib import admin
from .models import Contact, Management, Permission, Role

class ContactAdmin(admin.ModelAdmin):
    class Media:
        js = [
            "admin/js/jquery.init.js",  # Django admin jQuery
            "admin/js/filter_management.js",
        ]

admin.site.register(Contact, ContactAdmin)
admin.site.register(Management)
admin.site.register(Permission)
admin.site.register(Role)