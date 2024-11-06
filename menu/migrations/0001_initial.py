# Generated by Django 5.0.1 on 2024-11-05 19:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Назва')),
                ('url', models.CharField(blank=True, max_length=200, verbose_name='URL')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='menu.menu')),
            ],
            options={
                'verbose_name': 'Меню',
                'verbose_name_plural': 'Вкладене меню',
            },
        ),
    ]
