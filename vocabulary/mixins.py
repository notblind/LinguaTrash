from django.db.models import Q


class FilterQByCreatedMixin:
    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .filter(Q(create_id__isnull=True) | Q(create_id=self.request.user.id))
        )
