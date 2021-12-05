from django.contrib import admin

from .models import Vocabulary, Words, Translation, FeedBack, DayOfWeek, Holiday

# Register your models here.

admin.site.register(Vocabulary)
admin.site.register(Words)
admin.site.register(Translation)
admin.site.register(FeedBack)
admin.site.register(DayOfWeek)
admin.site.register(Holiday)