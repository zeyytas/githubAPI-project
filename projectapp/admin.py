from django.contrib import admin

from projectapp.models import Repositories, Language, Label

admin.site.register(Repositories)
admin.site.register(Label)
admin.site.register(Language)