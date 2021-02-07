# Generated by Django 3.1.5 on 2021-02-07 12:49

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_auto_20210111_2136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ['position']},
        ),
        migrations.RenameField(
            model_name='image',
            old_name='image_position',
            new_name='position',
        ),
        migrations.AlterField(
            model_name='place',
            name='long_description',
            field=tinymce.models.HTMLField(blank=True, verbose_name='Полное описание'),
        ),
    ]