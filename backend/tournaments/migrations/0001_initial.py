# Generated by Django 5.2.4 on 2025-07-29 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tournament',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField(blank=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='tournament_logos/')),
            ],
        ),
    ]
