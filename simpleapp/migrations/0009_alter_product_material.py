# Generated by Django 4.1.5 on 2023-04-25 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('simpleapp', '0008_alter_product_material'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='material',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='simpleapp.category'),
        ),
    ]
