# Generated by Django 3.0.2 on 2020-09-24 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ott', '0004_auto_20200923_1839'),
    ]

    operations = [
        migrations.AlterField(
            model_name='viewer',
            name='mobile',
            field=models.BigIntegerField(default=0),
            preserve_default=False,
        ),
    ]
