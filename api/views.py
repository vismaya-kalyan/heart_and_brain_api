from django.shortcuts import render
from rest_framework import viewsets
from .models import Characters
from .models import Comics
from .serializer import CharacterSerializer
from .serializer import ComicSerializer
from rest_framework import generics
 

class CharactersView(viewsets.ModelViewSet):
    queryset = Characters.objects.all()
    serializer_class = CharacterSerializer


class ComicsView(viewsets.ModelViewSet):
    queryset = Comics.objects.all()
    serializer_class = ComicSerializer
 

class CharacterList(generics.ListAPIView):
    serializer_class = ComicSerializer

    def get_queryset(self):
        charname = self.kwargs['charname']
        return Comics.objects.filter(characters__name__contains = charname)