# Generated by Django 5.1.6 on 2025-02-11 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ems_app', '0002_remove_employee_date_of_birth_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='user',
            new_name='username',
        ),
        migrations.AddField(
            model_name='employee',
            name='password',
            field=models.CharField(default='password', max_length=100),
        ),
    ]
