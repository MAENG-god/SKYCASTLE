from django.contrib import admin
from . models import Attendance

class BookAdmin(admin.ModelAdmin):
    list_display = ("pk", "date", "name")
# Register your models here.
admin.site.register(Attendance)