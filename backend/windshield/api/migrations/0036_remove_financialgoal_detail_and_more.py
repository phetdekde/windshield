# Generated by Django 4.0.1 on 2022-03-09 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0035_balancesheetlog_asset_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='financialgoal',
            name='detail',
        ),
        migrations.RemoveField(
            model_name='financialgoal',
            name='term',
        ),
        migrations.AddField(
            model_name='financialgoal',
            name='goal_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='financialgoal',
            name='icon',
            field=models.CharField(default='flag', max_length=30),
        ),
        migrations.AlterField(
            model_name='financialgoal',
            name='period_term',
            field=models.CharField(choices=[('DLY', 'Daily'), ('WLY', 'Weekly'), ('MLY', 'Monthly'), ('ALY', 'Annually')], max_length=3),
        ),
        migrations.AlterField(
            model_name='financialgoal',
            name='reward',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
