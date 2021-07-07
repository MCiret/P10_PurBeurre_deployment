from django.db import models


class Food(models.Model):
    barcode = models.CharField(primary_key=True, max_length=30)
    image_url = models.TextField()
    nutriment_url = models.TextField()
    nutri_score = models.CharField(max_length=1)
    name = models.CharField(max_length=150)
    off_url = models.TextField()

    def __str__(self):
        return f"Aliment --> {self.barcode} - {self.name} - {self.nutri_score} - {self.off_url}"


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    foods = models.ManyToManyField(Food)

    def __str__(self):
        return f"Catégorie --> {self.name}"