# Generated by Django 2.2.7 on 2020-01-20 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default='+2507445566667', max_length=15, null=True, unique=True),
        ),
    ]
