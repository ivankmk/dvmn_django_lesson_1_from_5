# Generated by Django 3.1.5 on 2021-01-11 21:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_auto_20210111_2101'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['image_order']},
        ),
        migrations.RenameField(
            model_name='image',
            old_name='my_order',
            new_name='image_order',
        ),
    ]
