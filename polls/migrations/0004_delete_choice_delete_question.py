# Generated by Django 4.2.7 on 2023-11-24 10:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
