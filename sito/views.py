from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from django.template.loader import render_to_string
from sito.models import *
from django.core.mail import send_mail
from filer.models import *

from datetime import datetime

# Create your views here.

def HomePage(request):
    post_list = Post.objects.all().order_by('-id')
    context = {'post_list':post_list}
    return render_to_response('index.html', context, context_instance=RequestContext(request))


def DetailView(request, post_id):
    post = Post.objects.get(pk=post_id)
    filer_list = Image.objects.filter(folder_id = post.album)
    context = {'post': post,
    			'filer_list':filer_list}
    return render_to_response('dettaglio.html', context, context_instance=RequestContext(request))


def categorie(request):
	categorie_list = Categorie.objects.all()
	context = {'categorie_list':categorie_list}
	return context
