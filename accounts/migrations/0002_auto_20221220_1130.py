# Generated by Django 3.0.7 on 2022-12-20 11:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='address_line_1',
            new_name='address_detail',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='address_line_2',
        ),
    ]
