# Generated by Django 4.0.1 on 2022-04-14 07:00

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0051_remove_knowledgearticle_isexclusive_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2022, 4, 14, 7, 0, 45, 3112, tzinfo=utc))),
            ],
        ),
        migrations.AlterField(
            model_name='balancesheetlog',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 4, 14, 7, 0, 44, 915424, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='dailyflowsheet',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 4, 14, 7, 0, 44, 999299, tzinfo=utc)),
        ),
    ]
