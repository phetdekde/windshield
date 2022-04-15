# Generated by Django 4.0.1 on 2022-04-14 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0050_knowledgearticle_isexclusive_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='knowledgearticle',
            name='isexclusive',
        ),
        migrations.AddField(
            model_name='knowledgearticle',
            name='exclusive_price',
            field=models.PositiveIntegerField(default=0),
        ),
    ]