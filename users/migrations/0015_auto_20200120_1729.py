# Generated by Django 2.2.7 on 2020-01-20 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20200120_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('INACTIVE', 'INACTIVE'), ('ACTIVE', 'ACTIVE')], default='INACTIVE', max_length=50),
        ),
    ]
