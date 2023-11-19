from django.db import models


class FeedBack(models.Model):
    text = models.TextField()
    partner_id = models.ForeignKey(
        "accounts.Partner", related_name="partner_u", on_delete=models.CASCADE
    )
    create_time = models.DateField(auto_now_add=True)


class DayOfWeek(models.Model):
    day_text = models.TextField()

    def __str__(self):
        return self.day_text

    class Meta:
        db_table = "dayofweek"


class Holiday(models.Model):
    day = models.ForeignKey(
        "DayOfWeek", related_name="dayofweek", on_delete=models.CASCADE
    )
    description = models.CharField(max_length=2048)

    def __str__(self):
        return self.description

    class Meta:
        db_table = "holiday"
