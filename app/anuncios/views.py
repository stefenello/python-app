from django.shortcuts import render, get_object_or_404
from .models import Anuncio
def anuncios_list(request):
    anuncios = Anuncio.objects.filter(estado="published")
    return render(request,
                  'anuncios.html',
                  {'anuncios': anuncios})