# Generated by Django 4.0.4 on 2022-06-07 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='dateResolved',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]