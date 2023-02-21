# Generated by Django 3.2.16 on 2023-01-18 19:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('public_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('name', models.CharField(max_length=200, null=True)),
                ('first_name', models.CharField(max_length=200, null=True)),
                ('last_name', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, unique=True)),
                ('clientEmail_1', models.CharField(default='None', max_length=200, null=True)),
                ('clientEmail_2', models.CharField(default='None', max_length=200, null=True)),
                ('clientEmail_3', models.CharField(default='None', max_length=200, null=True)),
                ('otp_code', models.CharField(max_length=6, null=True)),
                ('phone', models.CharField(max_length=200, null=True)),
                ('appsFlyer_appID', models.CharField(max_length=200, null=True)),
                ('appsFlyer_appToken', models.CharField(max_length=200, null=True)),
                ('fbSearch1', models.CharField(max_length=200, null=True)),
                ('fbSearch2', models.CharField(max_length=200, null=True)),
                ('fbSearch3', models.CharField(max_length=200, null=True)),
                ('fbSearch4', models.CharField(max_length=200, null=True)),
                ('fbSearch5', models.CharField(max_length=200, null=True)),
                ('playStoreSearch', models.CharField(max_length=200, null=True)),
                ('appSize', models.CharField(max_length=200, null=True)),
                ('adjustToken', models.CharField(max_length=200, null=True)),
                ('payoutAttributionWindow', models.CharField(max_length=200, null=True)),
                ('platformLogoUrl', models.CharField(default='https://pbs.twimg.com/profile_images/1455185376876826625/s1AjSxph_400x400.jpg', max_length=500, null=True)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]