from rest_framework import viewsets
from django.utils.translation import gettext_lazy as _

class AbstractViewSet(viewsets.ModelViewSet):
    ordering_fields = ["updated", "created"]
    ordering = ["-updated"]
