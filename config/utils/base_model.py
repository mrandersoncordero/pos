"""Base model."""

# Django
from django.db import models

# Utilities
import uuid


class BaseModel(models.Model):
    """
    Base Model.
    """

    # id = models.UUIDField(
    #     primary_key=True, default=uuid.uuid4, editable=False, unique=True
    # )

    created = models.DateTimeField(
        verbose_name="Creado",
        auto_now_add=True,
        help_text="Fecha y hora en que se creó el objeto",
    )

    modified = models.DateTimeField(
        verbose_name="Modificado",
        auto_now=True,
        help_text="Fecha en la que se modificó el objeto",
    )

    class Meta:
        """Meta options."""
        abstract = True
        ordering = ["-created"]