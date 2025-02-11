# Generated by Django 4.1.7 on 2024-01-25 13:15

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Allimage",
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
                ("patient_id", models.CharField(max_length=200)),
                ("nails", models.ImageField(null=True, upload_to="data/nails")),
                ("palm", models.ImageField(null=True, upload_to="data/palm")),
                ("full", models.ImageField(null=True, upload_to="data/full")),
                ("eye", models.ImageField(null=True, upload_to="data/eye")),
            ],
        ),
    ]
