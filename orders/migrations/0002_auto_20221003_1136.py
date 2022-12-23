# Generated by Django 3.0.7 on 2022-10-03 11:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address_line_1',
            new_name='amphoe',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='country',
            new_name='postal_code',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='state',
            new_name='tambon',
        ),
        migrations.RemoveField(
            model_name='order',
            name='address_line_2',
        ),
        migrations.AddField(
            model_name='order',
            name='address_detail',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]