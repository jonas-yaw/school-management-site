# Generated by Django 4.1 on 2022-08-31 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0002_rename_receipts_receipt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feescatalogue',
            name='student_class',
            field=models.CharField(max_length=20),
        ),
    ]
