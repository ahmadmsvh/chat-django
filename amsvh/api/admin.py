from django.contrib import admin

from guestcomment.models import Guest


class GuestAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'comment']
    # exclude = ('picture',)

admin.site.register(Guest, GuestAdmin)
