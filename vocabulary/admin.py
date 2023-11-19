from django.contrib import admin

from .models import Translation, Vocabulary, Word

admin.site.register(Vocabulary)
admin.site.register(Word)
admin.site.register(Translation)
