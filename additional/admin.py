from django.contrib import admin

from additional.models import DayOfWeek, FeedBack, Holiday

admin.site.register(FeedBack)
admin.site.register(DayOfWeek)
admin.site.register(Holiday)
