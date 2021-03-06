# Generated by Django 2.1.7 on 2019-04-26 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0013_subsorder_extra_cheese'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypeID_pasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='TypeID_platters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='TypeID_salads',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='TypeID_subs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=32)),
            ],
        ),
        migrations.AlterField(
            model_name='dinnerplatters',
            name='platters_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='platters_type', to='ordering.TypeID_platters'),
        ),
        migrations.AlterField(
            model_name='pasta',
            name='pasta_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pasta_type', to='ordering.TypeID_pasta'),
        ),
        migrations.AlterField(
            model_name='salads',
            name='salads_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salads_type', to='ordering.TypeID_salads'),
        ),
        migrations.AlterField(
            model_name='subs',
            name='subs_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subs_type', to='ordering.TypeID_subs'),
        ),
    ]
