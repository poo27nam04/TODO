# Generated by Django 3.2 on 2022-07-16 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_todomodel_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todomodel',
            old_name='created_by',
            new_name='owner',
        ),
    ]
