# Generated by Django 4.0.1 on 2022-02-26 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_financialstatementplan_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='id',
            field=models.CharField(max_length=19, primary_key=True, serialize=False),
        ),
    ]
