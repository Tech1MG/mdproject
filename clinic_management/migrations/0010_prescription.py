# Generated by Django 5.0.6 on 2024-06-01 16:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic_management', '0009_alter_diagnosis_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prescription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('note', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prescriptions', to='clinic_management.appointment')),
            ],
            options={
                'ordering': ('appointment',),
            },
        ),
    ]
