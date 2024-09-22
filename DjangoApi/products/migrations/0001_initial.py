# Generated by Django 5.1.1 on 2024-09-04 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=30)),
                ('price', models.DecimalField(decimal_places=1, default=0, max_digits=20)),
            ],
        ),
    ]
