# Generated by Django 5.0.4 on 2024-04-29 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0003_text_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='text',
            old_name='name',
            new_name='field',
        ),
    ]
