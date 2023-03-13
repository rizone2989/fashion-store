# Generated by Django 4.1.4 on 2023-01-23 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pyapp', '0004_catdb'),
    ]

    operations = [
        migrations.CreateModel(
            name='productdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
                ('price', models.CharField(blank=True, max_length=30, null=True)),
                ('quantity', models.IntegerField(blank=True, max_length=30, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='profile')),
                ('category', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]