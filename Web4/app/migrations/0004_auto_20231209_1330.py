# Generated by Django 2.2.28 on 2023-12-09 08:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20231209_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='posted',
            field=models.DateTimeField(db_index=True, default=datetime.datetime(2023, 12, 9, 13, 30, 0, 744466), verbose_name='Опубликована'),
        ),
    ]
