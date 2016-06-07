from __future__ import unicode_literals

from django.db import models

from image_cropping import ImageRatioField, ImageCropField

from datetime import datetime, timedelta, time, date
from django.utils.timesince import timesince

from filer.fields.image import FilerImageField
from filer.fields.file import FilerFileField
from filer.fields.folder import FilerFolderField

from django import forms

# Create your models here.

class Categorie(models.Model):
    titolo = models.CharField(max_length=100)
    sottotitolo = models.CharField(max_length=250, null=True, blank=True)

    def __unicode__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = "Categorie"



class Immagini(models.Model):
    titolo = models.CharField(max_length=100, verbose_name="Titolo:")
    image = models.ImageField(blank=True, null=True, upload_to='uploaded_images')
    didascalia = models.TextField(null=True, blank=True)
    cropping = ImageRatioField('image', '500x480')
    slider = ImageRatioField('image', '1920x1280')
    revolution = ImageRatioField('image', '1170x500', verbose_name="Revolution Gallery")
    thumb = ImageRatioField('image', '595x335', verbose_name="Miniatura")
    croplibero = ImageRatioField('image', '595x335', free_crop=True, verbose_name="Ritaglio Libero")
    croppinguno = ImageRatioField('image', '1140x487', free_crop=True)
    croppingdue = ImageRatioField('image', '198x132')
    croppingtre = ImageRatioField('image', '1199x674')
    pub_date = models.DateTimeField('date published')

    def image_img(self):
        if self.image:
            return u'<img src="%s" style="width:200px"/>' % self.image.url
        else:
            return '(Sin imagen)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

    def __unicode__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = "Galleria Immagini"
        ordering = ['id']




CSS_SLIDER = (
    ('0', 'stile uno'),
    ('1', 'stile due'),
                )
class Slider(models.Model):
    titolo = models.CharField(max_length=100, verbose_name="Titolo del Progetto:")
    image = models.ImageField(blank=True, null=True, upload_to='slider')
    scritta = models.TextField(null=True, blank=True)
    didascalia = models.TextField(null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    cropping = ImageRatioField('image', '500x480')
    slider = ImageRatioField('image', '1920x1280')
    revolution = ImageRatioField('image', '1170x500', verbose_name="Revolution Gallery")
    thumb = ImageRatioField('image', '595x335', verbose_name="Miniatura")
    croplibero = ImageRatioField('image', '595x335', free_crop=True, verbose_name="Ritaglio Libero")
    croppinguno = ImageRatioField('image', '1140x487', free_crop=True)
    croppingdue = ImageRatioField('image', '198x132')
    croppingtre = ImageRatioField('image', '1199x674')
    pub_date = models.DateTimeField('date published')
    impaginazione = models.CharField(choices=CSS_SLIDER, max_length=200, null=True, blank=True)
    active = models.BooleanField('attiva', 
                                    default=False)

    def image_img(self):
        if self.image:
            return u'<img src="%s" style="width:300px"/>' % self.image.url
        else:
            return '(Sin imagen)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

    def __unicode__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = "Slider"
        ordering = ['id']




class Video(models.Model):
    titolo = models.CharField("Titolo del Video:", max_length=100, null=True, blank=True)
    codice = models.CharField("Codice ID YouTube:", max_length=100, null=True, blank=True)
    youtubeurl = models.CharField("Indirizzo url youtube:", max_length=100, null=True, blank=True)
    start = models.IntegerField(default=0, null=True, blank=True, verbose_name="Punto di Partenza del Filmato in secondi")
    embedded = models.TextField("Codice Embedded YouTube", null=True, blank=True)
    thumb = models.ImageField(upload_to='uploaded_thumb_youtube', null=True, blank=True)
    link = models.CharField(max_length=100, null=True, blank=True)
    didascalia = models.TextField(null=True, blank=True)
 
    def __unicode__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = "Galleria Video"



FORMATI = (
    ('width-and-small', '400x400'),
    ('width-and-height', '400x791'),
    ('width-and-long', '800x400'),
    ('width-and-big', '800x638'),
    	)

class Post(models.Model):
    categoria = models.ForeignKey(Categorie, null=True, blank=True)
    titolo = models.CharField("Titolo:", max_length=100, null=True, blank=True)
    titolomenu = models.CharField("Titolo Menu:", max_length=100, null=True, blank=True)
    revhome = models.BooleanField('Home Gallery', 
                                    default=False, 
                                    help_text="Mostra IMG nella slide in home")
    introduzione = models.TextField(null=True, blank=True, verbose_name="Descrizione Breve per introduzione")
    body = models.TextField(null=True, blank=True, verbose_name="Descrizione")
    image = models.ImageField(blank=True, null=True, upload_to='pagine')
    impaginazione = models.CharField(choices=FORMATI, max_length=200, null=True, blank=True)
    thumb = ImageRatioField('image', '400x400', verbose_name="400x400px")
    thumb_due = ImageRatioField('image', '400x761', verbose_name="400x761px")
    thumb_tre = ImageRatioField('image', '800x400', verbose_name="800x400px")
    thumb_quattro = ImageRatioField('image', '800x638', verbose_name="800x638px")
    cropping = ImageRatioField('image', '1200x1200')
    slider = ImageRatioField('image', '1920x1280')
    revolution = ImageRatioField('image', '1170x500')
    croplibero = ImageRatioField('image', '595x335', free_crop=True, verbose_name="Ritaglio Libero")
    album = FilerFolderField(null=True, blank=True)
    video = models.ManyToManyField(Video, null=True, blank=True)
    galleria = models.ManyToManyField(Immagini, null=True, blank=True, verbose_name="Seleziona Immagini Galleria")
    pub_date = models.DateTimeField('date published')

    def image_img(self):
        if self.image:
            return u'<img src="%s" style="width:300px"/>' % self.image.url
        else:
            return '(Sin imagen)'
    image_img.short_description = 'Thumb'
    image_img.allow_tags = True

    def mystyle(self):
        size = self.impaginazione
        return size

    def myimage(self):
        if impaginazione == 'width-and-small':
            return self.thumb
        elif impaginazione == 'width-and-height':
            return self.thumb_due
        elif impaginazione == 'width-and-long':
            return self.thumb_tre
        elif impaginazione == 'width-and-big':
            return self.thumb_quattro
        else:
            return self.thumb
    
    def __unicode__(self):
        return self.titolo

    class Meta:
        verbose_name_plural = "Post"



