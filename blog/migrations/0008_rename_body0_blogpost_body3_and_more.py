# Generated by Django 4.0.1 on 2023-01-26 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blogcomment_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='body0',
            new_name='body3',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='heading0',
            new_name='heading3',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='shortSummary',
            field=models.CharField(default='Check this blog on <django.db.models.fields.CharField>', max_length=100),
        ),
    ]
