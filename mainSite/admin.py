from django.contrib import admin
from . import models


admin.site.register(models.Games)
admin.site.register(models.Order)
# Register your models here.
class GamesInline(admin.StackedInline):
    model = models.Games

class GamesAdmin(admin.ModelAdmin):
    inlines = [GamesInline]

admin.site.register(models.Category, GamesAdmin)