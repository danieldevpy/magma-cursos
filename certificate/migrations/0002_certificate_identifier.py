# Generated by Django 5.0.4 on 2024-04-26 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificate', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='identifier',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
