# Generated by Django 4.0.1 on 2022-03-07 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0030_alter_budget_cat_id_alter_dailyflow_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debt',
            name='debt_term',
            field=models.DateField(null=True),
        ),
    ]
