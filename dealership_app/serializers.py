from rest_framework import serializers
from .models import Dealer, Review

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "dealer", "review", "sentiment", "purchase_details",
                  "car_make", "car_model", "car_year", "purchase_date", "created_at"]

class DealerSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model = Dealer
        fields = ["id", "full_name", "short_name", "address", "city", "state",
                  "zip_code", "zip", "lat", "lng", "long", "reviews"]

    short_name = serializers.SerializerMethodField()
    zip = serializers.CharField(source="zip_code")
    long = serializers.FloatField(source="lng")

    def get_short_name(self, obj):
        return obj.full_name
