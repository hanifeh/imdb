# Generated by Django 3.2.9 on 2021-11-05 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genre', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=72)),
                ('director', models.CharField(max_length=72)),
                ('created_date', models.CharField(max_length=4)),
                ('long', models.PositiveIntegerField()),
                ('summery', models.TextField()),
                ('genre', models.ManyToManyField(to='genre.Genre')),
            ],
        ),
    ]