from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Dealer, Review
from .serializers import DealerSerializer, ReviewSerializer

@api_view(["GET"])
def dealers(request):
    state = request.GET.get("state")
    queryset = Dealer.objects.filter(state__iexact=state) if state else Dealer.objects.all()
    return Response(DealerSerializer(queryset, many=True).data)

@api_view(["GET"])
def dealer(request, dealer_id):
    try:
        return Response(DealerSerializer(Dealer.objects.get(id=dealer_id)).data)
    except Dealer.DoesNotExist:
        return Response({"error": "Dealer not found"}, status=404)

@api_view(["GET"])
def dealer_reviews(request, dealer_id):
    return Response(ReviewSerializer(Review.objects.filter(dealer_id=dealer_id), many=True).data)

@api_view(["GET"])
def car_makes(request):
    return Response([
        {"make": "Toyota", "models": ["Camry", "Corolla", "RAV4"]},
        {"make": "Honda", "models": ["Civic", "Accord", "CR-V"]},
        {"make": "Ford", "models": ["F-150", "Mustang", "Explorer"]},
    ])

@api_view(["POST"])
def analyze_review(request):
    text = request.data.get("text", "")
    positive_words = {"fantastic", "excellent", "great", "helpful", "friendly", "good"}
    sentiment = "positive" if any(word in text.lower() for word in positive_words) else "neutral"
    return Response({"text": text, "sentiment": sentiment})

@api_view(["POST"])
def register(request):
    required = ["username", "first_name", "last_name", "email", "password"]
    if any(not request.data.get(field) for field in required):
        return Response({"error": "All five fields are required"}, status=400)
    if User.objects.filter(username=request.data["username"]).exists():
        return Response({"error": "Username already exists"}, status=400)
    user = User.objects.create_user(
        username=request.data["username"], first_name=request.data["first_name"],
        last_name=request.data["last_name"], email=request.data["email"],
        password=request.data["password"])
    return Response({"message": "Registration successful", "username": user.username}, status=201)

@api_view(["POST"])
def login_user(request):
    user = authenticate(username=request.data.get("username"), password=request.data.get("password"))
    if user is None:
        return Response({"error": "Invalid credentials"}, status=401)
    login(request, user)
    return Response({"message": "Login successful", "username": user.username})

@api_view(["POST"])
def logout_user(request):
    logout(request)
    return Response({"message": "Logout successful"})

@api_view(["POST"])
def add_review(request, dealer_id):
    try:
        dealer = Dealer.objects.get(id=dealer_id)
    except Dealer.DoesNotExist:
        return Response({"error": "Dealer not found"}, status=404)
    text = request.data.get("review", "").strip()
    if not text:
        return Response({"error": "Review is required"}, status=400)
    sentiment = "positive" if any(word in text.lower() for word in ("fantastic", "excellent", "great")) else "neutral"
    item = Review.objects.create(dealer=dealer, user=request.user if request.user.is_authenticated else None,
                                 review=text, sentiment=sentiment)
    return Response(ReviewSerializer(item).data, status=status.HTTP_201_CREATED)

