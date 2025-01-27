# Generated by Django 5.0.4 on 2024-07-31 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="GlucoseRecord",
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
                ("device", models.CharField(max_length=255)),
                ("serial_number", models.CharField(max_length=255)),
                ("device_timestamp", models.DateTimeField()),
                ("record_type", models.CharField(max_length=255)),
                ("glucose_level", models.FloatField(blank=True, null=True)),
                ("glucose_scan", models.FloatField(blank=True, null=True)),
                (
                    "non_numeric_fast_insulin",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("fast_insulin_units", models.FloatField(blank=True, null=True)),
                (
                    "non_numeric_food_data",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("carbohydrates_grams", models.FloatField(blank=True, null=True)),
                ("carbohydrates_portions", models.FloatField(blank=True, null=True)),
                (
                    "non_numeric_long_acting_insulin",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                ("long_acting_insulin_units", models.FloatField(blank=True, null=True)),
                ("notes", models.TextField(blank=True, null=True)),
                ("glucose_test_strip", models.FloatField(blank=True, null=True)),
                ("ketone_level", models.FloatField(blank=True, null=True)),
                ("meal_insulin_units", models.FloatField(blank=True, null=True)),
                ("correction_insulin_units", models.FloatField(blank=True, null=True)),
                (
                    "user_adjusted_insulin_units",
                    models.FloatField(blank=True, null=True),
                ),
            ],
        ),
    ]
