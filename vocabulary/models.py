from django.db import models

# Create your models here.


class Vocabulary(models.Model):
    partner = models.ForeignKey(
        "accounts.Partner", related_name="partner", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=2048)
    create_time = models.DateField(auto_now_add=True)
    write_time = models.DateField(auto_now=True)
    like = models.BooleanField(default=False)

    class Meta:
        ordering = ["-like", "-id"]

    def __str__(self):
        return self.name


class Words(models.Model):
    vocabulary = models.ForeignKey(
        "Vocabulary", related_name="vocabulary", on_delete=models.CASCADE
    )
    word = models.CharField(max_length=2048)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.word


class Translation(models.Model):
    translate = models.CharField(max_length=2048)
    word = models.ForeignKey(
        "Words", related_name="word_realate", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.translate


class FeedBack(models.Model):
    text = models.TextField()
    partner = models.ForeignKey(
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
