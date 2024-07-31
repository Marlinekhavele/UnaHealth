# -*- coding: utf-8 -*-
import os
import django
import uuid
import sys
import csv
from pathlib import Path
from datetime import datetime


# Ensure the correct path to your settings module is set
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "unahealth.settings")
django.setup()

from app.models import GlucoseRecord

def convert_date_format(date_str):
    try:
        dt = datetime.strptime(date_str, '%d-%m-%Y %H:%M')
        return dt.strftime('%Y-%m-%d %H:%M:%S')
    except ValueError as e:
        print(f"Error converting date: {e}")
        return None

# Get the directory path from command line arguments
path = Path(sys.argv[1])
files_list = list(path.iterdir())  # List all files in the directory

for file_path in files_list:
    with open(file_path, "r", encoding="utf-8") as file:
        file.readline()  # Skip first line
        file.readline()  # Skip second line
        content_csv = csv.DictReader(file)
        print(content_csv.fieldnames)
        for row in content_csv:
            try:
                device_timestamp = convert_date_format(row['Gerätezeitstempel'])
                if device_timestamp is not None:
                    glucose_record = GlucoseRecord(
            device=row['Gerät'],
            serial_number=row['Seriennummer'],
            device_timestamp=device_timestamp,
            record_type=row['Aufzeichnungstyp'],
            glucose_level=row.get('Glukosewert-Verlauf mg/dL', None),
            glucose_scan=row.get('Glukose-Scan mg/dL', None),
            non_numeric_fast_insulin=row.get('Nicht numerisches schnellwirkendes Insulin', None),
            fast_insulin_units=row.get('Schnellwirkendes Insulin (Einheiten)', None),
            non_numeric_food_data=row.get('Nicht numerische Nahrungsdaten', None),
            carbohydrates_grams=row.get('Kohlenhydrate (Gramm)', None),
            carbohydrates_portions=row.get('Kohlenhydrate (Portionen)', None),
            non_numeric_long_acting_insulin=row.get('Nicht numerisches Depotinsulin', None),
            long_acting_insulin_units=row.get('Depotinsulin (Einheiten)', None),
            notes=row.get('Notizen', None),
            glucose_test_strip=row.get('Glukose-Teststreifen mg/dL', None),
            ketone_level=row.get('Keton mmol/L', None),
            meal_insulin_units=row.get('Mahlzeiteninsulin (Einheiten)', None),
            correction_insulin_units=row.get('Korrekturinsulin (Einheiten)', None),
            user_adjusted_insulin_units=row.get('Insulin-Änderung durch Anwender (Einheiten)', None),)
                    glucose_record.save()
            except KeyError as e:
                print(f"Missing expected column: {e}")
            except Exception as e:
                print(f"Error saving data: {e}")
            