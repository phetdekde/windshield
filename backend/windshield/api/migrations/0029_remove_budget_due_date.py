# Generated by Django 4.0.1 on 2022-03-06 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0028_rename_balance_budget_used_balance_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='budget',
            name='due_date',
        ),
    ]
