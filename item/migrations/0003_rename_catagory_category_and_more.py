# Generated by Django 4.2.11 on 2024-08-19 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_catagory_options_item'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Catagory',
            new_name='Category',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='catagory',
            new_name='category',
        ),
    ]
