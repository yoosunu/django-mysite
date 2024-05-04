from django.db import models


# Create your models here.
class Masterpiece(models.Model):
    """Model Definition for Masterpiece"""

    title = models.CharField(max_length=20)
    language = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )
    descripton = models.TextField()
    image = models.ImageField(
        null=True,
        blank=True,
    )
    file = models.FileField(
        null=True,
        blank=True,
    )
    register_only = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
