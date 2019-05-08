from django.db import models

from core.utils import ChoiceEnum


class DynamicPlacement(ChoiceEnum):
    html_head = "html_head"
    html_body_beginning = "html_body_beginning"
    content_beginning = "content_beginning"
    content_end = "content_end"


class DynamicHTML(models.Model):
    name = models.CharField(
        max_length=256,
    )
    content = models.TextField(
        null=True,
        blank=True,
    )
    placement = models.CharField(
        max_length=256,
        db_index=True,
        choices=DynamicPlacement.as_choices(),
    )

    is_active = models.BooleanField(
        default=True,
    )
    date_created = models.DateTimeField(
        auto_now_add=True,
    )
    date_modified = models.DateTimeField(
        auto_now=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Dynamic HTML"
        verbose_name_plural = "Dynamic HTML"