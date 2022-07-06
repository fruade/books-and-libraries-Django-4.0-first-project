# Generated by Django 4.0.5 on 2022-07-06 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_alter_library_options_alter_reader_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='readers',
            field=models.ManyToManyField(blank=True, null=True, to='library.reader', verbose_name='Читатели'),
        ),
        migrations.AlterUniqueTogether(
            name='subscription',
            unique_together={('id_reader', 'id_library')},
        ),
    ]
