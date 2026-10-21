from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [("dealership_app", "0002_seed_dealership_data")]
    operations = [
        migrations.AddField("review", "purchase_details", models.CharField(default="Verified vehicle purchase", max_length=200)),
        migrations.AddField("review", "car_make", models.CharField(default="Toyota", max_length=80)),
        migrations.AddField("review", "car_model", models.CharField(default="Camry", max_length=80)),
        migrations.AddField("review", "car_year", models.PositiveIntegerField(default=2024)),
        migrations.AddField("review", "purchase_date", models.DateField(blank=True, null=True)),
    ]
