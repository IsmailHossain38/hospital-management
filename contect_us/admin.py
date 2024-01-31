from django.contrib import admin
from .models import ContectUs
# Register your models here.

#admin panel e table head e name show korte amra ata use korte pari
class ContectModelAdmin(admin.ModelAdmin):
    list_display =['id','name','phone','problem']
    
admin.site.register(ContectUs , ContectModelAdmin)
