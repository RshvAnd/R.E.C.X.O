# Generated by Django 4.1.2 on 2023-08-13 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_order_software'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoftwareType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('software_type', models.CharField(max_length=200)),
            ],
        ),
    ]
