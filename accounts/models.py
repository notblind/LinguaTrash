from crum import get_current_user
from django.contrib.auth.models import User
from django.db import models


class AccountMixin(models.Model):
    create_id = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        default=None,
        related_name="created_%(class)s",
        db_column="create_id",
    )
    write_id = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        default=None,
        related_name="modified_%(class)s",
        db_column="write_id",
    )
    create_date = models.DateField(auto_now_add=True)
    write_date = models.DateField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.create_id = user
        self.write_id = user
        super().save(*args, **kwargs)
