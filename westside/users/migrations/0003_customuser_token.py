# Generated by Django 4.1 on 2022-08-25 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_customuser_phonenumber_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='token',
            field=models.CharField(default=None, max_length=22),
        ),
    ]