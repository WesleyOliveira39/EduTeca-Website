# Generated by Django 2.2.12 on 2021-11-27 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0014_auto_20211126_2238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livro',
            old_name='arquivo',
            new_name='capa',
        ),
    ]
