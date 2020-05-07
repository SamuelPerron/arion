# Generated by Django 3.0.6 on 2020-05-06 22:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('partners', '0004_auto_20200506_2255'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='parent_partner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='partners.Partner'),
            preserve_default=False,
        ),
    ]
