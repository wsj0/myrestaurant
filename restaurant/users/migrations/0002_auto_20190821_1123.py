# Generated by Django 2.0 on 2019-08-21 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='org',
            field=models.CharField(max_length=128, verbose_name='Organization'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='telephone',
            field=models.CharField(max_length=50, verbose_name='Telephone'),
        ),
    ]
