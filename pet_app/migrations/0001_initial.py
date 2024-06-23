# Generated by Django 5.0.6 on 2024-06-17 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('age', models.IntegerField(default=1)),
                ('fullness', models.IntegerField(default=40)),
                ('happiness', models.IntegerField(default=40)),
                ('is_resting', models.BooleanField(default=False)),
            ],
        ),
    ]
