# Generated by Django 3.0.2 on 2020-09-04 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ott', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='languages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(max_length=800)),
            ],
        ),
        migrations.AlterField(
            model_name='viewer',
            name='mobile',
            field=models.IntegerField(),
        ),
    ]
