from django.contrib import admin
from .models import Masterpiece


# Register your models here.
@admin.register(Masterpiece)
class MasterpieceAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "descripton",
        "language",
        "register_only",
    )

    list_filter = (
        "language",
        "register_only",
    )
    search_fields = ("language",)
