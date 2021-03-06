# Generated by Django 4.0.1 on 2022-01-13 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='age',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='family',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='points',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='province',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='user.province'),
        ),
    ]
