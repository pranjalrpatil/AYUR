# Generated by Django 3.0.7 on 2021-12-03 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0008_expense_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='expense',
            name='month',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expense',
            name='year',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
    ]
