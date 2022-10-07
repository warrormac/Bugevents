# Generated by Django 3.2.16 on 2022-10-07 13:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PointOfSale",
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
                (
                    "name",
                    models.CharField(
                        help_text="Provider contact name.", max_length=50, unique=True
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Provider",
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
                (
                    "ruc",
                    models.CharField(
                        help_text="Provider RUC.",
                        max_length=11,
                        unique=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[0-9]*$", "Only numeric characters are allowed."
                            )
                        ],
                    ),
                ),
                (
                    "company_name",
                    models.CharField(help_text="Provider name.", max_length=30),
                ),
                (
                    "contact_number",
                    models.CharField(
                        help_text="Provider phone number.",
                        max_length=9,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[0-9]*$", "Only numeric characters are allowed."
                            )
                        ],
                    ),
                ),
                (
                    "contact_name",
                    models.CharField(
                        help_text="Provider contact name.",
                        max_length=50,
                        validators=[
                            django.core.validators.RegexValidator(
                                "^[a-zA-Z]*$", "Only alphabetic characters are allowed."
                            )
                        ],
                    ),
                ),
            ],
        ),
    ]
