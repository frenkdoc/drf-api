# Generated by Django 3.1.6 on 2021-02-15 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20210215_1538'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Journalis',
            new_name='Journalist',
        ),
    ]
