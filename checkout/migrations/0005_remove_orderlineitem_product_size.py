# Generated by Django 3.1.4 on 2021-01-03 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_auto_20210103_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderlineitem',
            name='product_size',
        ),
    ]
