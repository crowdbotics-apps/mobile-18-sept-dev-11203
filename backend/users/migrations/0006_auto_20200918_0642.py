# Generated by Django 2.2.16 on 2020-09-18 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_auto_20200918_0638"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="gfghfg",
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="user",
            name="hjgjhgjg",
            field=models.DecimalField(
                blank=True, decimal_places=10, max_digits=30, null=True
            ),
        ),
    ]
