__author__ = 'ray'

from django.contrib import admin
from database.models import CommonUser, ManageUser, Institution

admin.site.register(CommonUser)
admin.site.register(ManageUser)
admin.site.register(Institution)
