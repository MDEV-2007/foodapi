from django.db import models

class Category(models.Model):
    category = models.CharField(max_length=150)

    def __str__(self):
        return self.category

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/",blank=True,null=True)
    avibale = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    

    def __str__(self):
        return self.name