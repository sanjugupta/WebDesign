from django.contrib import admin

from sito.models import *
from image_cropping import ImageCroppingMixin


class MyModelAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

class SliderAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("image_img", "titolo", "active")

class ImmaginiAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("image_img", "titolo")

def get_category(self):
    return self.categoria.all()
class PostAdmin(ImageCroppingMixin, admin.ModelAdmin):
    list_display = ("image_img", "titolo")



admin.site.register(Categorie, MyModelAdmin)
admin.site.register(Immagini, ImmaginiAdmin)
admin.site.register(Video, MyModelAdmin)
admin.site.register(Post, PostAdmin)
