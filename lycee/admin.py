from django.contrib import admin
from .models import Student,Cursus,Presence

admin.site.site_header="page d'administration du lycée"
# Register your models here.
class studentAdmin(admin.ModelAdmin):
  list_display = ("first_name", "last_name", "email", 'phone' )

class CursusAdmin(admin.ModelAdmin):
  fields = ["scholar_year","name","year_from_bac"]

class PresenceAdmin(admin.ModelAdmin):
  fields =  ["date_call","Reasson","ismissing","student"]

admin.site.register(Student,studentAdmin)
admin.site.register(Cursus,CursusAdmin)
admin.site.register(Presence,PresenceAdmin)
