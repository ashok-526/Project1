# Generated by Django 5.1.4 on 2024-12-26 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0025_alter_student_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='department',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_id',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='StudentID',
        ),
    ]
