from rest_framework import serializers
from .models import Dealer, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "dealer", "review", "sentiment", "created_at"]

class DealerSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Dealer
        fields = ["id", "full_name", "address", "city", "state", "zip_code", "lat", "lng", "reviews"]

