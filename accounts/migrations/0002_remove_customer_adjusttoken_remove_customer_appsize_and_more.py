# Generated by Django 4.0.1 on 2023-01-26 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='adjustToken',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='appSize',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='appsFlyer_appID',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='appsFlyer_appToken',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='clientEmail_1',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='clientEmail_2',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='clientEmail_3',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='fbSearch1',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='fbSearch2',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='fbSearch3',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='fbSearch4',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='fbSearch5',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='payoutAttributionWindow',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='platformLogoUrl',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='playStoreSearch',
        ),
    ]