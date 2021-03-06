# Generated by Django 4.0.1 on 2022-05-04 00:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_rename_timestamp_verifycodelog_send_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='verifycodelog',
            name='ref_code',
            field=models.CharField(default=0, max_length=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='newuser',
            name='is_verify',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterModelTable(
            name='verifycodelog',
            table='verify_code_log',
        ),
        migrations.CreateModel(
            name='VerifyTokenLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=32)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('code_log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.verifycodelog')),
            ],
            options={
                'db_table': 'verify_token_log',
            },
        ),
    ]
