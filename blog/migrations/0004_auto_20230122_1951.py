# Generated by Django 3.2.16 on 2023-01-22 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_tilte_blogpost_title'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='chead0',
            new_name='body0',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='chead1',
            new_name='body1',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='chead2',
            new_name='body2',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='head0',
            new_name='heading0',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='head1',
            new_name='heading1',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='head2',
            new_name='heading2',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='post_id',
            new_name='postId',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='pub_date',
            new_name='publishDate',
        ),
    ]
