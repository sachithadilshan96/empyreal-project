# Generated by Django 3.0.8 on 2020-08-21 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_auto_20200815_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='is_verified',
            field=models.BooleanField(default=True),
        ),
    ]
