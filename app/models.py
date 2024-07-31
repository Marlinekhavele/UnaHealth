import uuid
from django.db import models


# Create your models here.
class GlucoseRecord(models.Model):
    device = models.CharField(max_length=255)  # Gerät
    serial_number = models.CharField(max_length=255)  # Seriennummer
    device_timestamp = models.DateTimeField()  # Gerätezeitstempel
    record_type = models.CharField(max_length=255)  # Aufzeichnungstyp
    glucose_level = models.FloatField(null=True, blank=True)  # Glukosewert-Verlauf mg/dL
    glucose_scan = models.FloatField(null=True, blank=True)  # Glukose-Scan mg/dL
    non_numeric_fast_insulin = models.CharField(max_length=255, null=True, blank=True)  # Nicht numerisches schnellwirkendes Insulin
    fast_insulin_units = models.FloatField(null=True, blank=True)  # Schnellwirkendes Insulin (Einheiten)
    non_numeric_food_data = models.CharField(max_length=255, null=True, blank=True)  # Nicht numerische Nahrungsdaten
    carbohydrates_grams = models.FloatField(null=True, blank=True)  # Kohlenhydrate (Gramm)
    carbohydrates_portions = models.FloatField(null=True, blank=True)  # Kohlenhydrate (Portionen)
    non_numeric_long_acting_insulin = models.CharField(max_length=255, null=True, blank=True)  # Nicht numerisches Depotinsulin
    long_acting_insulin_units = models.FloatField(null=True, blank=True)  # Depotinsulin (Einheiten)
    notes = models.TextField(null=True, blank=True)  # Notizen
    glucose_test_strip = models.FloatField(null=True, blank=True)  # Glukose-Teststreifen mg/dL
    ketone_level = models.FloatField(null=True, blank=True)  # Keton mmol/L
    meal_insulin_units = models.FloatField(null=True, blank=True)  # Mahlzeiteninsulin (Einheiten)
    correction_insulin_units = models.FloatField(null=True, blank=True)  # Korrekturinsulin (Einheiten)
    user_adjusted_insulin_units = models.FloatField(null=True, blank=True)  # Insulin-Änderung durch Anwender (Einheiten)

    def __str__(self):
        return f"{self.device} - {self.serial_number} - {self.device_timestamp}"