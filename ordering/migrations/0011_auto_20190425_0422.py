# Generated by Django 2.1.7 on 2019-04-25 01:22

from django.db import migrations, models
import django.db.models.deletion
import ordering.models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0010_auto_20190412_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pizzaorder',
            name='toppings',
        ),
        migrations.AddField(
            model_name='pizzaorder',
            name='toppings_1',
            field=models.ForeignKey(default=ordering.models.none_toppings, on_delete=django.db.models.deletion.CASCADE, related_name='toppings_1', to='ordering.Toppings'),
        ),
        migrations.AddField(
            model_name='pizzaorder',
            name='toppings_2',
            field=models.ForeignKey(default=ordering.models.none_toppings, on_delete=django.db.models.deletion.CASCADE, related_name='toppings_2', to='ordering.Toppings'),
        ),
        migrations.AddField(
            model_name='pizzaorder',
            name='toppings_3',
            field=models.ForeignKey(default=ordering.models.none_toppings, on_delete=django.db.models.deletion.CASCADE, related_name='toppings_3', to='ordering.Toppings'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='cart_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
