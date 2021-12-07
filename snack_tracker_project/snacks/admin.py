from django.contrib import admin

from snacks.models import Snack

# Register your models here.
#@admin.register(Snack)
#class AdminSnack(admin.ModelAdmin):
#    list_display=['name','purchaser']


admin.site.register(Snack)


