from django.contrib import admin
from .models import *
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin

class opportunityResource(resources.ModelResource):
    class Meta:
        model = opportunity

class opportunityAdmin(ImportExportModelAdmin):
    resource_class = opportunityResource

admin.site.register(User)
admin.site.register(opportunity,opportunityAdmin)
admin.site.register(save)
admin.site.register(mails)
