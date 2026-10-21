from django.db import migrations

def seed_data(apps, schema_editor):
    Dealer = apps.get_model("dealership_app", "Dealer")
    Review = apps.get_model("dealership_app", "Review")
    dealers = [
        (1, "Sunrise Motors", "1200 Main Street", "Kansas City", "KS", "66101", 39.0997, -94.5786),
        (2, "Prairie Auto Group", "4550 East Central Avenue", "Wichita", "KS", "67208", 37.6872, -97.3301),
        (3, "Lone Star Cars", "800 Congress Avenue", "Austin", "TX", "78701", 30.2672, -97.7431),
    ]
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

