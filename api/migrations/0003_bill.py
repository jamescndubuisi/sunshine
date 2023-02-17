# Generated by Django 4.1.7 on 2023-02-16 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_discount_created_discount_updated_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('source', models.CharField(max_length=200)),
                ('message', models.CharField(max_length=200)),
                ('seen', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
