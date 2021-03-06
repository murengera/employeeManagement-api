# Generated by Django 2.2.7 on 2020-01-20 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20200120_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='national_id',
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('INACTIVE', 'INACTIVE'), ('ACTIVE', 'ACTIVE')], default='INACTIVE', max_length=50),
        ),
    ]
