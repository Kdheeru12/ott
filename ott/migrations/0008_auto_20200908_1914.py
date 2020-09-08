# Generated by Django 3.0.2 on 2020-09-08 13:44

from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('ott', '0007_auto_20200908_1528'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movies',
            name='my_field2',
        ),
        migrations.AlterField(
            model_name='movies',
            name='genre',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Drama', 'Drama'), ('Comedy', 'Comedy'), ('Action', 'Action'), ('Horror', 'Horror'), ('Family', 'Family'), ('Thriller', 'Thriller'), ('Adventures', 'Adventures'), ('ScienceFiction', 'ScienceFiction')], max_length=68, null=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='language',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='ott.Languages'),
        ),
    ]
