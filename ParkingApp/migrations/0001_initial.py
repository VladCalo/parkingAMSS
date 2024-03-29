# Generated by Django 4.2.7 on 2024-01-13 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Credentials",
            fields=[
                ("credentials_id", models.AutoField(primary_key=True, serialize=False)),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "Credentials",
            },
        ),
        migrations.CreateModel(
            name="Floor",
            fields=[
                ("floor_id", models.AutoField(primary_key=True, serialize=False)),
                ("floor_number", models.IntegerField()),
            ],
            options={
                "db_table": "Floor",
            },
        ),
        migrations.CreateModel(
            name="ParkDetails",
            fields=[
                (
                    "park_details_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("address", models.CharField(max_length=255)),
                ("latitude", models.DecimalField(decimal_places=6, max_digits=9)),
                ("longitude", models.DecimalField(decimal_places=6, max_digits=9)),
                ("height_limit", models.IntegerField(default=2)),
                ("weigh_limit", models.IntegerField(default=3500)),
            ],
            options={
                "db_table": "ParkingDetails",
            },
        ),
        migrations.CreateModel(
            name="ParkingSlot",
            fields=[
                (
                    "parking_slot_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("slot_number", models.IntegerField()),
                ("has_charger", models.BooleanField()),
                ("physical_available", models.BooleanField(default=False)),
                ("standard_price", models.IntegerField(default=10)),
                (
                    "floor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ParkingApp.floor",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ParkOwner",
            fields=[
                ("park_owner_id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "ParkOwner",
            },
        ),
        migrations.CreateModel(
            name="Users",
            fields=[
                ("user_id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=100)),
                ("last_name", models.CharField(max_length=100)),
                ("number_plate", models.CharField(max_length=100)),
                ("vehicle_type", models.CharField(max_length=200)),
                ("verified", models.BooleanField()),
                (
                    "credentials",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ParkingApp.credentials",
                    ),
                ),
            ],
            options={
                "db_table": "Users",
            },
        ),
        migrations.CreateModel(
            name="ParkingSlotRules",
            fields=[
                (
                    "parking_slot_rules_id",
                    models.AutoField(primary_key=True, serialize=False),
                ),
                ("date_start_rule", models.DateTimeField()),
                ("date_end_rule", models.DateTimeField()),
                ("price", models.FloatField()),
                (
                    "parking_slot",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ParkingApp.parkingslot",
                    ),
                ),
            ],
            options={
                "db_table": "ParkingSlotRules",
            },
        ),
        migrations.CreateModel(
            name="Park",
            fields=[
                ("park_id", models.AutoField(primary_key=True, serialize=False)),
                ("total_spots", models.IntegerField()),
                ("no_floors", models.IntegerField()),
                (
                    "park_details",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ParkingApp.parkdetails",
                    ),
                ),
                (
                    "park_owner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ParkingApp.parkowner",
                    ),
                ),
            ],
            options={
                "db_table": "Park",
            },
        ),
        migrations.AddField(
            model_name="floor",
            name="park",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="ParkingApp.park"
            ),
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                ("booking_id", models.AutoField(primary_key=True, serialize=False)),
                ("booking_start_date", models.DateTimeField()),
                ("booking_end_date", models.DateTimeField()),
                ("price", models.FloatField()),
                (
                    "parking_slot",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ParkingApp.parkingslot",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ParkingApp.users",
                    ),
                ),
            ],
            options={
                "db_table": "Booking",
            },
        ),
    ]
