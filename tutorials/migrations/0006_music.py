# Generated by Django 4.0.1 on 2022-01-16 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0005_komplekt_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Music',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(default='', max_length=200)),
                ('description', models.TextField(default='', max_length=2000)),
            ],
        ),
    ]
