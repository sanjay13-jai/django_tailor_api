# Generated by Django 5.0.7 on 2024-07-24 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_register_cookies'),
    ]

    operations = [
        migrations.AddField(
            model_name='login',
            name='IPAddress',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='login',
            name='browserName',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='login',
            name='browserVersion',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='login',
            name='deviceType',
            field=models.CharField(max_length=45, null=True),
        ),
        migrations.AddField(
            model_name='login',
            name='isLoggedIn',
            field=models.BooleanField(default=False, help_text='1-True, 0-False'),
        ),
        migrations.AddField(
            model_name='login',
            name='logInTime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='login',
            name='logOutTime',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='register',
            name='isLoggedIn',
            field=models.BooleanField(default=False, help_text='1-True, 0-False'),
        ),
        migrations.AddField(
            model_name='register',
            name='resetToken',
            field=models.CharField(default='ABCDEFGH', max_length=100),
        ),
        migrations.AddField(
            model_name='register',
            name='resetTokenTime',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
