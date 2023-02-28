# Generated by Django 3.2.3 on 2021-06-13 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_report'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnostic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=122)),
                ('name', models.CharField(max_length=122)),
                ('phone', models.CharField(max_length=12)),
                ('tests', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
