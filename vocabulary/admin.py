from django.contrib import admin
from .models import Vocabulary, Words, Translation

# Register your models here.

admin.site.register(Vocabulary)
admin.site.register(Words)
admin.site.register(Translation)