# Generated by Django 4.1.2 on 2023-09-02 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_getjob_qualification_alter_order_soft_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='soft_time',
        ),
        migrations.RemoveField(
            model_name='order',
            name='soft_type',
        ),
        migrations.AlterField(
            model_name='order',
            name='software',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
