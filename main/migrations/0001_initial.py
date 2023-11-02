# Generated by Django 4.2.7 on 2023-11-02 07:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocomotivePart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('schema_id', models.CharField(max_length=100, verbose_name='Чертежный номер')),
                ('russian_name', models.CharField(max_length=100, verbose_name='Название на русском')),
                ('chinese_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Название на китайском')),
                ('quantity', models.CharField(blank=True, max_length=100, null=True, verbose_name='Количество')),
                ('description', models.CharField(blank=True, max_length=500, null=True, verbose_name='Описание')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='main.locomotivepart', verbose_name='Родительская схема')),
            ],
        ),
    ]