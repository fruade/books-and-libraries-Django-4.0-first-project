# Generated by Django 4.0.5 on 2022-07-07 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_alter_library_readers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='library',
            name='readers',
            field=models.ManyToManyField(blank=True, related_name='readers_library', to='library.reader', verbose_name='Читатели'),
        ),
    ]