# Generated by Django 3.2.7 on 2022-01-07 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0021_rename_about_us_heading_index_about_us_headings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='index',
            old_name='about_us_headings',
            new_name='about_us_heading',
        ),
    ]
