from django.contrib import admin

from .models import (
    DayOfWeek,
    FeedBack,
    Holiday,
    Translation,
    Vocabulary,
    Words,
)

# Register your models here.

admin.site.register(Vocabulary)
admin.site.register(Words)
admin.site.register(Translation)
admin.site.register(FeedBack)
admin.site.register(DayOfWeek)
admin.site.register(Holiday)
