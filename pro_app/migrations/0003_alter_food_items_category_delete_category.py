# Generated by Django 4.2.2 on 2023-06-16 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro_app', '0002_category_alter_food_items_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food_items',
            name='category',
            field=models.CharField(choices=[('Buff', 'Buff'), ('Chicken', 'Chicken'), ('Veg', 'Vegetarian')], max_length=20),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
