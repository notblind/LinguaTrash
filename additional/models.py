from django.db import models

from accounts.models import AccountMixin


class FeedBack(AccountMixin):
    text = models.TextField()


class DayOfWeek(AccountMixin):
    day_text = models.TextField()

    def __str__(self):
        return self.day_text


class Holiday(AccountMixin):
    day = models.ForeignKey(
        "DayOfWeek", related_name="dayofweek", on_delete=models.CASCADE
    )
    description = models.CharField(max_length=2048)

    def __str__(self):
        return self.description
