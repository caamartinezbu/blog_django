from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, CreateView, UpdateView, DeleteView)
from .models import Entry
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

# Create your views here.


class LockedView(LoginRequiredMixin):
    login_url = 'admin:login'

class EntryListView(LockedView, ListView):
    model = Entry
    # devolverá sus entradas en orden ascendente, con la entrada más reciente en la parte superior de la lista.
    queryset = Entry.objects.all().order_by("-data_created")

class EntryDetailView(LockedView, DetailView):
    model = Entry


class EntryCreateView(LockedView, SuccessMessageMixin, CreateView):
    model = Entry
    fields = ["title", "content"]
    success_url = reverse_lazy("entry-list")
    success_message = "¡Tu nueva publicación fue creada!"


class EntryUpdateView(LockedView, SuccessMessageMixin, UpdateView):
    model = Entry
    fields = ["title", "content"]
    success_message = " ¡Tu publicación fue actualizada!"

    def get_success_url(self):
      
        return reverse_lazy(
            "entry-detail",
            kwargs = { "pk": self.object.pk }
        )
    
class EntryDeleteView(LockedView, DeleteView):
    model = Entry
    success_url  = reverse_lazy("entry-list")
    success_message = "¡Tu publicación fue eliminada!"

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super().delete(request, *args, **kwargs)

