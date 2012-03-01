from django.contrib import admin
from apps.personal_info.models import Person


class PersonAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'birth', 'contacts', 'jabber', 'pk')

admin.site.register(Person, PersonAdmin)
