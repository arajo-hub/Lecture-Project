# Generated by Django 3.0.3 on 2020-03-10 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='shcool',
            new_name='school',
        ),
    ]