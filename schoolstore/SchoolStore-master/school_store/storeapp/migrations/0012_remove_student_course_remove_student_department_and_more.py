# Generated by Django 4.2.7 on 2023-11-09 09:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('storeapp', '0011_alter_student_course'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='course',
        ),
        migrations.RemoveField(
            model_name='student',
            name='department',
        ),
        migrations.RemoveField(
            model_name='student',
            name='materials_provide',
        ),
        migrations.RemoveField(
            model_name='student',
            name='purpose',
        ),
        migrations.DeleteModel(
            name='Material',
        ),
    ]
