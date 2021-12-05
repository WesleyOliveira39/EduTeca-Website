# Generated by Django 2.2.12 on 2021-12-02 04:46

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0024_auto_20211201_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='livro',
            name='capa',
            field=django_resized.forms.ResizedImageField(crop=None, default='../static/img/sem_capa.jpg', force_format=None, keep_meta=True, quality=80, size=[200, 292], upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='categoria',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='cadastros.Categoria'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='edicao',
            field=models.IntegerField(blank=True, default=1, null=True, verbose_name='Edição'),
        ),
        migrations.AlterField(
            model_name='livro',
            name='editora',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]