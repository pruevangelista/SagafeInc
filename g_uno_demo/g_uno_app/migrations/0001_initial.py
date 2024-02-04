# Generated by Django 4.2.9 on 2024-02-03 16:36

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "client_ID",
                    models.IntegerField(
                        primary_key=True,
                        serialize=False,
                        validators=[django.core.validators.MaxValueValidator(999999)],
                    ),
                ),
                ("client_name", models.CharField(max_length=55)),
                ("client_address", models.CharField(max_length=255)),
                ("client_TIN", models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name="DeliveryReceipt",
            fields=[
                ("dr_number", models.AutoField(primary_key=True, serialize=False)),
                ("dr_date", models.DateField(default=datetime.date.today)),
                ("dr_due_date", models.DateField(default=datetime.date.today)),
                (
                    "dr_terms",
                    models.CharField(
                        choices=[("90", "90"), ("120", "120")], max_length=3
                    ),
                ),
                ("dr_amt_wo_vat", models.FloatField(blank=True, default=0)),
                ("dr_amt_vat", models.FloatField(blank=True, default=0)),
                (
                    "client",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="delivery_receipts",
                        to="g_uno_app.client",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "product_ID",
                    models.IntegerField(
                        primary_key=True,
                        serialize=False,
                        validators=[django.core.validators.MaxValueValidator(999999)],
                    ),
                ),
                ("product_name", models.CharField(max_length=55)),
                ("code", models.CharField(max_length=3)),
                ("type", models.CharField(max_length=30)),
                ("size", models.CharField(max_length=20)),
                ("unit", models.CharField(max_length=20)),
                ("unit_price", models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name="QuantityOrdered",
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
                ("quantity", models.IntegerField()),
                (
                    "dr",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="g_uno_app.deliveryreceipt",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="g_uno_app.product",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="deliveryreceipt",
            name="product_id",
            field=models.ManyToManyField(
                blank=True, through="g_uno_app.QuantityOrdered", to="g_uno_app.product"
            ),
        ),
    ]
