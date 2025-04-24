from django.db import models

# Create your models here.
class Country(models.Model):
    country_name = models.CharField(max_length=100, unique=True)
    country_code = models.CharField(max_length=10, unique=True)
    region = models.CharField(max_length=100, null=True)
    income_group = models.CharField(max_length=50, null=True)
    is_country = models.BooleanField(default=True)

class Data(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    year = models.IntegerField()
    emission = models.FloatField()

    class Meta:
        unique_together = ('country', 'year')

class Feedback(models.Model):
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback from {self.email} on {self.submitted_at.strftime('%Y-%m-%d %H:%M')}"
