# Generated by Django 3.1.4 on 2021-10-01 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ['-payment_time']},
        ),
    ]