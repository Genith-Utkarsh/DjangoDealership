from django.contrib import admin
from .models import Dealer, Review

admin.site.register([Dealer, Review])

