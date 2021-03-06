# Generated by Django 4.0.1 on 2022-05-02 21:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_newuser_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='newuser',
            name='is_verify',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='VerifyCodeLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=6)),
                ('activity', models.CharField(max_length=30)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'VerifyCodeLog',
            },
        ),
    ]
