# Generated by Django 2.1.7 on 2019-04-10 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0007_auto_20190409_1731'),
    ]

    operations = [
        migrations.CreateModel(
            name='Condiments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('condiment', models.CharField(max_length=64)),
            ],
        ),
        migrations.RenameField(
            model_name='pastaorder',
            old_name='subs',
            new_name='pasta',
        ),
        migrations.RenameField(
            model_name='salads',
            old_name='salad_type',
            new_name='salads_type',
        ),
        migrations.AddField(
            model_name='subsorder',
            name='condiments',
            field=models.ManyToManyField(blank=True, related_name='subs_condiments', to='ordering.Condiments'),
        ),
    ]
