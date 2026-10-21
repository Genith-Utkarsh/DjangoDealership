from django.contrib.auth.models import User
from django.db import models

class Dealer(models.Model):
    id = models.IntegerField(primary_key=True)
    full_name = models.CharField(max_length=160)
    address = models.CharField(max_length=240)
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=10)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)

    def __str__(self):
        return self.full_name

class Review(models.Model):
    dealer = models.ForeignKey(Dealer, related_name="reviews", on_delete=models.CASCADE)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    review = models.TextField()
    sentiment = models.CharField(max_length=20, default="positive")
    created_at = models.DateTimeField(auto_now_add=True)

