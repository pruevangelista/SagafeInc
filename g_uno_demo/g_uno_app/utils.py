from django.db import connection
from .models import *


def get_next(model):
    with connection.cursor() as cursor:
        # Get the next auto-increment value from information_schema
        cursor.execute(f"SELECT AUTO_INCREMENT FROM information_schema.TABLES WHERE TABLE_SCHEMA = DATABASE() AND TABLE_NAME = '{model._meta.db_table}'")
        row = cursor.fetchone()
        return row[0]