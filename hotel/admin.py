from copyreg import dispatch_table
from django.contrib import admin
from .models import Rooms, Users
from import_export.admin import ImportExportModelAdmin

# from django.dispatch import receiver
# from import_export.signals import post_export

# @receiver(post_export, dispatch_uid='ba')
# def _post_ecport(model, **kwargs):

#     pass

# admin.site.register(Rooms)
admin.site.register(Users)




# Register your models here.

from import_export import resources
from hotel.models import Rooms

class BookResource(resources.ModelResource):

    class Meta:
        model = Rooms


class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource

admin.site.register(Rooms, BookAdmin)