# Generated by Django 5.1.6 on 2025-02-14 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionPaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('qno', models.IntegerField(unique=True)),
                ('question', models.TextField()),
            ],
        ),
    ]
