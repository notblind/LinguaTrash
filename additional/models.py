from django.db import models

from accounts.models import AccountMixin


class FeedBack(AccountMixin):
    text = models.TextField()


class Holiday(AccountMixin):
    day = models.DateField(auto_now_add=True)
    description = models.CharField(max_length=2048)

    def __str__(self):
        return self.description
