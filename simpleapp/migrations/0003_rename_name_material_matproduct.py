# Generated by Django 4.1.5 on 2023-04-21 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0002_material_productmaterial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='material',
            old_name='name',
            new_name='matproduct',
        ),
    ]
