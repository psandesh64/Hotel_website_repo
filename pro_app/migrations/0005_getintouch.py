# Generated by Django 4.2.2 on 2023-06-19 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro_app', '0004_category_alter_food_items_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='GetInTouch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('choose_option', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('text_area', models.TextField()),
            ],
        ),
    ]
