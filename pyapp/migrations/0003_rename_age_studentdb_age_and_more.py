# Generated by Django 4.1.4 on 2023-01-21 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pyapp', '0002_alter_studentdb_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentdb',
            old_name='Age',
            new_name='age',
        ),
        migrations.RenameField(
            model_name='studentdb',
            old_name='Image',
            new_name='image',
        ),
        migrations.RenameField(
            model_name='studentdb',
            old_name='Name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='studentdb',
            old_name='Phone',
            new_name='phone',
        ),
    ]
