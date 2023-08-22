from django.shortcuts import render
from django.views.generic import (ListView, DetailView)
from .models import Entry
# Create your views here.


class EntryListView(ListView):
    model = Entry
    # devolverá sus entradas en orden ascendente, con la entrada más reciente en la parte superior de la lista.
    queryset = Entry.objects.all().order_by("-data_created")

class EntryDetailView(DetailView):
    model = Entry

