# Generated by Django 5.0.4 on 2024-05-04 13:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("masterpieces", "0002_masterpiece_language_alter_masterpiece_file_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="masterpiece",
            name="register_only",
            field=models.BooleanField(default=False),
        ),
    ]