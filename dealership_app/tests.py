from django.test import TestCase
from .models import Dealer

class DealershipApiTests(TestCase):
    fixtures = []

    def setUp(self):
        Dealer.objects.create(id=99, full_name="Test Motors", address="1 Test Way",
                              city="Kansas City", state="KS", zip_code="66101")

    def test_filter_dealers_by_state(self):
        response = self.client.get("/api/dealers?state=KS")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(any(item["full_name"] == "Test Motors" for item in response.json()))

    def test_analyze_review(self):
        response = self.client.post("/api/analyze-review", {"text": "Fantastic services"},
                                    content_type="application/json")
        self.assertEqual(response.json()["sentiment"], "positive")
