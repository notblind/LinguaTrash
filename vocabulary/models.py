from django.db import models


class Vocabulary(models.Model):
    partner_id = models.ForeignKey(
        "accounts.Partner", related_name="vocabularies", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=2048)
    create_time = models.DateField(auto_now_add=True)
    write_time = models.DateField(auto_now=True)
    like = models.BooleanField(default=False)

    class Meta:
        ordering = ["-like", "-id"]

    def __str__(self):
        return self.name


class Word(models.Model):
    vocabulary_id = models.ForeignKey(
        "Vocabulary", related_name="words", on_delete=models.CASCADE
    )
    word = models.CharField(max_length=2048)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.word


class Translation(models.Model):
    translate = models.CharField(max_length=2048)
    word_id = models.ForeignKey(
        "Word", related_name="translations", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.translate
