# Generated by Django 5.1.6 on 2025-02-21 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.TextField()),
                ('category', models.CharField(max_length=100)),
                ('stock', models.IntegerField()),
                ('quantity', models.IntegerField(default=1)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('customer_name', models.CharField(max_length=255)),
                ('customer_email', models.EmailField(max_length=254, unique=True)),
                ('customer_phone', models.CharField(max_length=15)),
            ],
        ),
    ]
