# Generated by Django 4.2.16 on 2024-12-04 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calculator',
            name='action',
        ),
        migrations.AddField(
            model_name='calculator',
            name='hint',
            field=models.CharField(choices=[('+', 'Plus'), ('-', 'Minus'), ('/', 'Bulish'), ('*', 'Kupaytirish')], default='+', max_length=1, verbose_name='Amal'),
        ),
        migrations.AddField(
            model_name='calculator',
            name='value_1',
            field=models.FloatField(null=True, verbose_name='1chi qiymat'),
        ),
        migrations.AddField(
            model_name='calculator',
            name='value_2',
            field=models.FloatField(null=True, verbose_name='1chi qiymat'),
        ),
    ]