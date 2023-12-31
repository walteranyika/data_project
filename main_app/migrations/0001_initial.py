# Generated by Django 4.2.7 on 2023-11-06 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('dob', models.DateField(null=True)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=7)),
                ('disabled', models.BooleanField(default=False)),
            ],
        ),
    ]
