# Generated by Django 2.2.12 on 2021-11-27 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0011_auto_20211126_0539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='livro',
            name='arquivo',
        ),
        migrations.AddField(
            model_name='livro',
            name='capa',
            field=models.ImageField(blank=True, null=True, upload_to='img/'),
        ),
    ]