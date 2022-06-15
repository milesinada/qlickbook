# Generated by Django 4.0.4 on 2022-06-15 01:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('description', models.TextField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('dateCreated', models.DateTimeField(default=django.utils.timezone.now)),
                ('dateResolved', models.DateTimeField(blank=True, null=True)),
                ('difficulty', models.IntegerField(choices=[(0, 'Easy'), (1, 'Normal'), (2, 'HARD')], default=0)),
                ('status', models.IntegerField(choices=[(0, 'Not Started'), (1, 'In Progress'), (2, 'Completed')], default=0)),
                ('commentary', models.TextField(max_length=256)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
    ]
