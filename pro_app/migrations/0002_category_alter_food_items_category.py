# Generated by Django 4.2.2 on 2023-06-16 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pro_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('Buff', 'Buff'), ('Chicken', 'Chicken'), ('Vegetarian', 'Veg')], max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='food_items',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categori', to='pro_app.category'),
        ),
    ]