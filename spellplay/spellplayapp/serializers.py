from rest_framework import serializers
from spellplayapp.models import Score

class ScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Score

    # def get_validation_exclusions(self):
    #     exclusions = super(ScoreSerializer, self).get_validation_exclusions()
    #     return exclusions + ['final_score']
