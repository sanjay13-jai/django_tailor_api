# Generated by Django 5.0.7 on 2024-08-31 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_rename_ankle_circumference_bottommeasurement_anklecircumference_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bottommeasurement',
            name='bottomType',
            field=models.CharField(default='abcd', max_length=40),
        ),
        migrations.AddField(
            model_name='bottommeasurement',
            name='quantity',
            field=models.CharField(default='abcd', max_length=40),
        ),
        migrations.AddField(
            model_name='topmeasurement',
            name='quantity',
            field=models.CharField(default='40', max_length=40),
        ),
        migrations.AddField(
            model_name='topmeasurement',
            name='topType',
            field=models.CharField(default='abcd', max_length=40),
        ),
    ]
