# Generated by Django 4.0.5 on 2022-07-07 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FeedBack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
                ('surname', models.CharField(max_length=30)),
                ('rating', models.PositiveIntegerField()),
                ('feedback', models.TextField()),
            ],
        ),
    ]
