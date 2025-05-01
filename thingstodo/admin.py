from django.contrib import admin

from .models import thingstodo


class thingstodoAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "body",
        "author",
    ]
admin.site.register(thingstodo)

#admin.site.register(thingstodo, thingstodoAdmin)