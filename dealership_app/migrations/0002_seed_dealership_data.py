from django.db import migrations

def seed_data(apps, schema_editor):
    Dealer = apps.get_model("dealership_app", "Dealer")
    Review = apps.get_model("dealership_app", "Review")
    User = apps.get_model("auth", "User")
    if not User.objects.filter(username="root").exists():
        User.objects.create_superuser("root", "root@django-dealership.com", "password")
    dealers = [
        (1, "Sunrise Motors", "1200 Main Street", "Kansas City", "KS", "66101", 39.0997, -94.5786),
        (2, "Prairie Auto Group", "4550 East Central Avenue", "Wichita", "KS", "67208", 37.6872, -97.3301),
        (3, "Lone Star Cars", "800 Congress Avenue", "Austin", "TX", "78701", 30.2672, -97.7431),
    ]
    cities = [("Topeka", "KS", "66601"), ("Lawrence", "KS", "66044"),
              ("Overland Park", "KS", "66204"), ("Olathe", "KS", "66061")]
    for dealer_id in range(4, 51):
        city, state, zip_code = cities[(dealer_id - 4) % len(cities)]
        dealers.append((dealer_id, f"Heartland Auto {dealer_id}", f"{100 + dealer_id} Market Street",
                        city, state, zip_code, 38.9 + dealer_id / 1000, -95.6 - dealer_id / 1000))
    for values in dealers:
        dealer = Dealer.objects.create(
            id=values[0], full_name=values[1], address=values[2], city=values[3],
            state=values[4], zip_code=values[5], lat=values[6], lng=values[7])
        if dealer.id == 1:
            Review.objects.create(dealer=dealer, review="Fantastic services", sentiment="positive")

def remove_data(apps, schema_editor):
    apps.get_model("dealership_app", "Dealer").objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [("dealership_app", "0001_initial")]
    operations = [migrations.RunPython(seed_data, remove_data)]
