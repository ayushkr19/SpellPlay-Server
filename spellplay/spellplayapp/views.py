from django.shortcuts import render
from rest_framework import generics
from spellplayapp.models import Score
from spellplayapp.serializers import ScoreSerializer

# Create your views here.
class ScoreList(generics.ListCreateAPIView):
    """
    List scores & allow creation
    """
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
