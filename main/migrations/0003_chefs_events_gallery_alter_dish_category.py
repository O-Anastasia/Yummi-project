# Generated by Django 5.0.4 on 2024-04-28 20:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_dishcategory_options_dish'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chefs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('position', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='chefs/')),
            ],
            options={
                'verbose_name': 'Кухар',
                'verbose_name_plural': 'Кухари',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='events/')),
            ],
            options={
                'verbose_name': 'Подія',
                'verbose_name_plural': 'Події',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='gallery/')),
            ],
            options={
                'verbose_name': 'Фото',
                'verbose_name_plural': 'Фото',
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='dish',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dishes', to='main.dishcategory'),
        ),
    ]