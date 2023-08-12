# Generated by Django 4.2 on 2023-08-12 06:29

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("message_text1", models.CharField(max_length=200)),
                ("message_text2", models.CharField(max_length=200)),
                ("message_text3", models.CharField(max_length=200)),
                ("message_writer", models.CharField(max_length=20)),
            ],
        ),
    ]
