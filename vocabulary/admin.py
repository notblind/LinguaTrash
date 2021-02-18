from django.contrib import admin
from .models import Vocabulary, Words, Translation, FeedBack

# Register your models here.

admin.site.register(Vocabulary)
admin.site.register(Words)
admin.site.register(Translation)
admin.site.register(FeedBack)