# Generated by Django 4.2.3 on 2023-11-17 08:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_blogs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogs',
            old_name='timestamp',
            new_name='timeStamp',
        ),
    ]