# Generated by Django 4.1 on 2024-06-20 20:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("preview", "0006_alter_user_area"),
    ]

    operations = [
        migrations.CreateModel(
            name="Equipment",
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
                ("name", models.CharField(max_length=50)),
                ("brand", models.CharField(max_length=50)),
                ("model", models.CharField(max_length=50)),
                ("serial_number", models.CharField(max_length=150)),
                ("fabrication_year", models.CharField(max_length=10)),
                ("adquisition_year", models.CharField(max_length=10)),
                (
                    "area",
                    models.CharField(
                        choices=[
                            ("uci", "UCI"),
                            ("cardio", "Cardiologia"),
                            ("nefro", "Nefrologia"),
                            ("quiro", "Quirofano"),
                            ("radio", "Radiologia"),
                            ("gral", "General"),
                        ],
                        default="gral",
                        max_length=20,
                    ),
                ),
                (
                    "location",
                    models.CharField(
                        choices=[
                            ("uci", "UCI"),
                            ("cardio", "Cardiologia"),
                            ("nefro", "Nefrologia"),
                            ("quiro", "Quirofano"),
                            ("radio", "Radiologia"),
                            ("gral", "General"),
                        ],
                        default="gral",
                        max_length=20,
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("op", "En operacion"),
                            ("cm", "Mantenimiento correctivo"),
                            ("pm", "Mantenimiento preventivo"),
                            ("os", "Fuera de"),
                        ],
                        default="op",
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="user",
            name="area",
            field=models.CharField(
                choices=[
                    ("uci", "UCI"),
                    ("cardio", "Cardiologia"),
                    ("nefro", "Nefrologia"),
                    ("quiro", "Quirofano"),
                    ("radio", "Radiologia"),
                    ("gral", "General"),
                ],
                default="gral",
                max_length=20,
            ),
        ),
    ]
