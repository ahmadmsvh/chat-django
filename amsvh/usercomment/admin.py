from django.contrib import admin

from .models import UserComment, Picture


class UserCommentAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'username','comment']


class PictureAdmin(admin.ModelAdmin):

    exclude = ('picture','content_type')

admin.site.register(UserComment, UserCommentAdmin)
admin.site.register(Picture, PictureAdmin)
