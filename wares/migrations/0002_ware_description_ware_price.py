# Generated by Django 4.1.7 on 2023-02-24 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wares', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ware',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='ware',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]