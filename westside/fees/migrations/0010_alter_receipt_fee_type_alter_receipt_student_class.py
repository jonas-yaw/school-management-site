# Generated by Django 4.1 on 2022-09-12 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0009_alter_feescatalogue_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receipt',
            name='fee_type',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='receipt',
            name='student_class',
            field=models.CharField(max_length=50),
        ),
    ]