# Generated by Django 2.2.5 on 2019-10-06 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memes', '0003_auto_20191003_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mem',
            name='text',
            field=models.TextField(blank=True, max_length=3000),
        ),
    ]