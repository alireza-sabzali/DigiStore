from django.db import models


class DraftManager(models.Manager):
    def get_queryset(self):
        return super(DraftManager, self).get_queryset().filter(status='draft')
