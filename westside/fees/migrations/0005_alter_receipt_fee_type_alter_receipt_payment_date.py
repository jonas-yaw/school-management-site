# Generated by Django 4.1 on 2022-09-01 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0004_feescatalogue_fee_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='fee_type',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='payment_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
