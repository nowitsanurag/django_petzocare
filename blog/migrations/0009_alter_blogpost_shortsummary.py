# Generated by Django 4.0.1 on 2023-01-26 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_rename_body0_blogpost_body3_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='shortSummary',
            field=models.CharField(default='Click below link to read the article.', max_length=100),
        ),
    ]
