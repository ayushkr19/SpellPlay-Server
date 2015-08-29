from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
class Score(models.Model):

    def __str__(self):
        return self.num_wrong_words + ", " + self.created_at

    total_words = models.IntegerField()
    num_wrong_words = models.IntegerField()
    num_incorrect_start_words = models.IntegerField()
    final_score = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-final_score']
