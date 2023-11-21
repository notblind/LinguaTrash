from django.db import models

from accounts.models import AccountMixin


class Vocabulary(AccountMixin):
    name = models.CharField(max_length=2048)
    like = models.BooleanField(default=False)

    class Meta:
        ordering = ["-like", "-id"]

    def __str__(self):
        return self.name


class Word(AccountMixin):
    vocabulary_id = models.ForeignKey(
        "Vocabulary", related_name="words", on_delete=models.CASCADE
    )
    word = models.CharField(max_length=2048)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.word


class Translation(AccountMixin):
    translate = models.CharField(max_length=2048)
    word_id = models.ForeignKey(
        "Word", related_name="translations", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.translate
