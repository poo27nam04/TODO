# Generated by Django 3.2 on 2022-07-15 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_auto_20220715_2136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todomodel',
            name='tid',
        ),
        migrations.AddField(
            model_name='todomodel',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
