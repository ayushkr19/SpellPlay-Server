from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from spellplayapp import views

urlpatterns = [
    url(r'^scores/$', views.ScoreList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
