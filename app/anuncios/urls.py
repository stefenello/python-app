from django.urls import path
from . import views
app_name = 'anuncios'
urlpatterns = [
    # post views
    path('', views.anuncios_list, name='anuncios_list')
]