# Generated by Django 3.0.5 on 2021-06-26 08:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gym', '0013_contact_full_name_c'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer_database',
            name='Year',
        ),
        migrations.RemoveField(
            model_name='trainers',
            name='TYear',
        ),
    ]
