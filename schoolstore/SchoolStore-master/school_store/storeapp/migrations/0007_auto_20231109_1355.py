# Generated by Django 3.1.7 on 2023-11-09 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0006_auto_20231109_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.CharField(choices=[], max_length=20),
        ),
    ]
