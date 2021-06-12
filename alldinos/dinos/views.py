from django.views.generic import ListView, DetailView
from .models import Dinosaur


class DinosaurListView(ListView):
    model = Dinosaur

class DinosaurDetailView(DetailView):
    model = Dinosaur