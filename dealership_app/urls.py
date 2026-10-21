from django.urls import path
from . import views

urlpatterns = [
    path("dealers", views.dealers),
    path("dealers/<int:dealer_id>", views.dealer),
    path("dealers/<int:dealer_id>/reviews", views.dealer_reviews),
    path("dealers/<int:dealer_id>/reviews/add", views.add_review),
    path("car-makes", views.car_makes),
    path("analyze-review", views.analyze_review),
    path("register", views.register),
    path("login", views.login_user),
    path("logout", views.logout_user),
    path("fetchDealers", views.fetch_dealers),
    path("fetchDealers/<str:state>", views.fetch_dealers),
    path("fetchDealer/<int:dealer_id>", views.fetch_dealer),
    path("fetchReviews/dealer/<int:dealer_id>", views.fetch_reviews),
    path("djangoapp/get_cars", views.get_cars),
    path("analyze/<path:text>", views.analyze_path),
    path("djangoapp/login", views.login_user),
    path("djangoapp/logout", views.logout_user),
]
