from django.db import models
from django.shortcuts import render
from django.views.generic import ListView , DeleteView

from snacks.models import Snack

# Create your views here.

class SnackListView(ListView) :
    template_name ='home.html'
    model = Snack


class SnackDetailView(DeleteView):
    template_name = 'snack_detail.html'
    model= Snack

