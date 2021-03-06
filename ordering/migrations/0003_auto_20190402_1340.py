# Generated by Django 2.1.7 on 2019-04-02 10:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ordering', '0002_auto_20190331_1808'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='DinnerPlatters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platters_type', models.CharField(max_length=100)),
                ('platters_price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('platters_size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='platters_size', to='ordering.SizeID')),
            ],
        ),
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pasta_type', models.CharField(max_length=100)),
                ('pasta_price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Salads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salad_type', models.CharField(max_length=100)),
                ('salads_price', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.RenameField(
            model_name='pizza',
            old_name='price',
            new_name='pizza_price',
        ),
        migrations.RenameField(
            model_name='pizza',
            old_name='size',
            new_name='pizza_size',
        ),
        migrations.RenameField(
            model_name='subs',
            old_name='size',
            new_name='subs_size',
        ),
        migrations.AddField(
            model_name='subs',
            name='subs_price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cart',
            name='pasta_order',
            field=models.ManyToManyField(blank=True, related_name='pasta_order', to='ordering.Pasta'),
        ),
        migrations.AddField(
            model_name='cart',
            name='pizza_order',
            field=models.ManyToManyField(blank=True, related_name='pizza_order', to='ordering.Pizza'),
        ),
        migrations.AddField(
            model_name='cart',
            name='platter_order',
            field=models.ManyToManyField(blank=True, related_name='platters_order', to='ordering.DinnerPlatters'),
        ),
        migrations.AddField(
            model_name='cart',
            name='salads_order',
            field=models.ManyToManyField(blank=True, related_name='salads_order', to='ordering.Salads'),
        ),
        migrations.AddField(
            model_name='cart',
            name='subs_order',
            field=models.ManyToManyField(blank=True, related_name='subs_order', to='ordering.Subs'),
        ),
        migrations.AddField(
            model_name='cart',
            name='topping_order',
            field=models.ManyToManyField(blank=True, related_name='topping_order', to='ordering.Toppings'),
        ),
        migrations.AddField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
