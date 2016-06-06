# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 10:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import filer.fields.folder
import image_cropping.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('filer', '0004_auto_20160328_1434'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=100)),
                ('sottotitolo', models.CharField(blank=True, max_length=250, null=True)),
            ],
            options={
                'verbose_name_plural': 'Categorie',
            },
        ),
        migrations.CreateModel(
            name='Immagini',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=100, verbose_name='Titolo:')),
                ('image', models.ImageField(blank=True, null=True, upload_to='uploaded_images')),
                ('didascalia', models.TextField(blank=True, null=True)),
                ('cropping', image_cropping.fields.ImageRatioField('image', '500x480', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='cropping')),
                ('slider', image_cropping.fields.ImageRatioField('image', '1920x1280', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='slider')),
                ('revolution', image_cropping.fields.ImageRatioField('image', '1170x500', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Revolution Gallery')),
                ('thumb', image_cropping.fields.ImageRatioField('image', '595x335', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Miniatura')),
                ('croplibero', image_cropping.fields.ImageRatioField('image', '595x335', adapt_rotation=False, allow_fullsize=False, free_crop=True, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Ritaglio Libero')),
                ('croppinguno', image_cropping.fields.ImageRatioField('image', '1140x487', adapt_rotation=False, allow_fullsize=False, free_crop=True, help_text=None, hide_image_field=False, size_warning=True, verbose_name='croppinguno')),
                ('croppingdue', image_cropping.fields.ImageRatioField('image', '198x132', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='croppingdue')),
                ('croppingtre', image_cropping.fields.ImageRatioField('image', '1199x674', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='croppingtre')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Galleria Immagini',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(blank=True, max_length=100, null=True, verbose_name='Titolo:')),
                ('titolomenu', models.CharField(blank=True, max_length=100, null=True, verbose_name='Titolo Menu:')),
                ('revhome', models.BooleanField(default=False, help_text='Mostra IMG nella slide in home', verbose_name='Home Gallery')),
                ('introduzione', models.TextField(blank=True, null=True, verbose_name='Descrizione Breve per introduzione')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Descrizione')),
                ('image', models.ImageField(blank=True, null=True, upload_to='pagine')),
                ('impaginazione', models.CharField(blank=True, choices=[('width-and-small', '400x400'), ('width-and-height', '400x791'), ('width-and-long', '800x400'), ('width-and-big', '800x638')], max_length=200, null=True)),
                ('thumb', image_cropping.fields.ImageRatioField('image', '400x400', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='400x400px')),
                ('thumb_due', image_cropping.fields.ImageRatioField('image', '400x761', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='400x761px')),
                ('thumb_tre', image_cropping.fields.ImageRatioField('image', '800x400', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='800x400px')),
                ('thumb_quattro', image_cropping.fields.ImageRatioField('image', '800x638', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='800x638px')),
                ('cropping', image_cropping.fields.ImageRatioField('image', '1200x1200', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='cropping')),
                ('slider', image_cropping.fields.ImageRatioField('image', '1920x1280', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='slider')),
                ('revolution', image_cropping.fields.ImageRatioField('image', '1170x500', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='revolution')),
                ('croplibero', image_cropping.fields.ImageRatioField('image', '595x335', adapt_rotation=False, allow_fullsize=False, free_crop=True, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Ritaglio Libero')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('album', filer.fields.folder.FilerFolderField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='filer.Folder')),
                ('categoria', models.ManyToManyField(blank=True, null=True, to='sito.Categorie')),
                ('galleria', models.ManyToManyField(blank=True, null=True, to='sito.Immagini', verbose_name='Seleziona Immagini Galleria')),
            ],
            options={
                'verbose_name_plural': 'Post',
            },
        ),
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(max_length=100, verbose_name='Titolo del Progetto:')),
                ('image', models.ImageField(blank=True, null=True, upload_to='slider')),
                ('scritta', models.TextField(blank=True, null=True)),
                ('didascalia', models.TextField(blank=True, null=True)),
                ('link', models.TextField(blank=True, null=True)),
                ('cropping', image_cropping.fields.ImageRatioField('image', '500x480', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='cropping')),
                ('slider', image_cropping.fields.ImageRatioField('image', '1920x1280', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='slider')),
                ('revolution', image_cropping.fields.ImageRatioField('image', '1170x500', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Revolution Gallery')),
                ('thumb', image_cropping.fields.ImageRatioField('image', '595x335', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Miniatura')),
                ('croplibero', image_cropping.fields.ImageRatioField('image', '595x335', adapt_rotation=False, allow_fullsize=False, free_crop=True, help_text=None, hide_image_field=False, size_warning=True, verbose_name='Ritaglio Libero')),
                ('croppinguno', image_cropping.fields.ImageRatioField('image', '1140x487', adapt_rotation=False, allow_fullsize=False, free_crop=True, help_text=None, hide_image_field=False, size_warning=True, verbose_name='croppinguno')),
                ('croppingdue', image_cropping.fields.ImageRatioField('image', '198x132', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='croppingdue')),
                ('croppingtre', image_cropping.fields.ImageRatioField('image', '1199x674', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=True, verbose_name='croppingtre')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('impaginazione', models.CharField(blank=True, choices=[('0', 'stile uno'), ('1', 'stile due')], max_length=200, null=True)),
                ('active', models.BooleanField(default=False, verbose_name='attiva')),
            ],
            options={
                'ordering': ['id'],
                'verbose_name_plural': 'Slider',
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titolo', models.CharField(blank=True, max_length=100, null=True, verbose_name='Titolo del Video:')),
                ('codice', models.CharField(blank=True, max_length=100, null=True, verbose_name='Codice ID YouTube:')),
                ('youtubeurl', models.CharField(blank=True, max_length=100, null=True, verbose_name='Indirizzo url youtube:')),
                ('start', models.IntegerField(blank=True, default=0, null=True, verbose_name='Punto di Partenza del Filmato in secondi')),
                ('embedded', models.TextField(blank=True, null=True, verbose_name='Codice Embedded YouTube')),
                ('thumb', models.ImageField(blank=True, null=True, upload_to='uploaded_thumb_youtube')),
                ('link', models.CharField(blank=True, max_length=100, null=True)),
                ('didascalia', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Galleria Video',
            },
        ),
        migrations.AddField(
            model_name='post',
            name='video',
            field=models.ManyToManyField(blank=True, null=True, to='sito.Video'),
        ),
    ]
