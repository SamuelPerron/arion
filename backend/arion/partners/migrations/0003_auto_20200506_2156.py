# Generated by Django 3.0.6 on 2020-05-06 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0002_auto_20200506_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='line2',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
