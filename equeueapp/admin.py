from django.contrib import admin

import equeueapp.models as models

class CabinetAdmin(admin.ModelAdmin):
    list_display = ('cabinetid', 'name')

class QueueAdmin(admin.ModelAdmin):
    list_display = ('queueid', 'cabinetid', 'priority')

admin.site.register(models.Cabinet, CabinetAdmin)
admin.site.register(models.Queue, QueueAdmin)