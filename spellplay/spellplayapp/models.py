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

    # Added to ensure validation occurs
    def save(self, **kwargs):
        self.clean()
        return super(Score, self).save(**kwargs)

    # Add validation to the score
    def clean(self):
        if self.final_score != (10 * self.total_words - 2 * self.num_wrong_words - 5 * self.num_incorrect_start_words):
            raise ValidationError({'final_score':'Invalid final score'})
