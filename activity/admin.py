__author__ = 'ray'

from django.contrib import admin
from database.models import ActivityInfo, ActivityRegister, ActivityComment

admin.site.register(ActivityInfo)
admin.site.register(ActivityRegister)
admin.site.register(ActivityComment)
