# Generated by Django 4.1.7 on 2023-03-20 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('cooking_time', models.FloatField(help_text='In minutes')),
                ('ingredients', models.CharField(max_length=350)),
                ('description', models.TextField()),
            ],
        ),
    ]