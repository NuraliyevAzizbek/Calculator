# Generated by Django 4.2.16 on 2024-12-17 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0004_hints_alter_calculator_value_2'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Hints',
        ),
        migrations.AlterField(
            model_name='calculator',
            name='value_2',
            field=models.FloatField(help_text='0 bulishi mumkin emas', null=True, verbose_name='2chi qiymat'),
        ),
    ]