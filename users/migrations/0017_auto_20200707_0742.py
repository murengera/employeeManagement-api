# Generated by Django 2.2.7 on 2020-07-07 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20200121_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('INACTIVE', 'INACTIVE'), ('ACTIVE', 'ACTIVE')], default='ACTIVE', max_length=50),
        ),
    ]