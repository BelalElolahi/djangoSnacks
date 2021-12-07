from django.db import models
from django.shortcuts import render
from django.views.generic import ListView , DeleteView ,DetailView , UpdateView ,CreateView

from snacks.models import Snack
from django.urls.base import reverse_lazy


# Create your views here.

class SnackListView(ListView) :
    template_name ='home.html'
    model = Snack


class SnackDetailView(DetailView):
    template_name = 'snack_detail.html'
    model= Snack


class SnackDeleteView(DeleteView):
    template_name = 'thing_confirm_delete.html'
    model = Snack
    success_url  = reverse_lazy('home')


class SnackCreateView(CreateView):
    template_name = 'snack_create.html'
    model= Snack
    fields = ['name','description','purchaser']


class SnackUpdateView(UpdateView):
    template_name = 'snack_update.html'
    model= Snack
    fields=['name','description']


     
