# Generated by Django 2.2.16 on 2020-09-18 06:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0002_load_initial_data"),
        ("users", "0007_auto_20200918_0648"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="vnbvnv",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_vnbvnv",
                to="home.CustomText",
            ),
        ),
    ]
