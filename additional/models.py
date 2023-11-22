from django.db import models

from accounts.models import AccountMixin


class FeedBack(AccountMixin):
    text = models.TextField()


class DayOfWeek(AccountMixin):
    day_text = models.TextField()

    def __str__(self):
        return self.day_text


class Holiday(AccountMixin):
    day_id = models.ForeignKey(
        "DayOfWeek",
        related_name="dayofweek",
        on_delete=models.CASCADE,
        db_column="day_id",
    )
    description = models.CharField(max_length=2048)

    def __str__(self):
        return self.description
