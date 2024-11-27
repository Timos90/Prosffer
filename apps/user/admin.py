from django.contrib import admin
from . import models


class ConsumerAdmin(admin.ModelAdmin):
    list_display =  ['user', 'phone_number', 'date_of_birth', 'address'] 


admin.site.register(models.Consumer, ConsumerAdmin)
