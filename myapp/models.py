from django.db import models

class Category(models.Model):

    name = models.CharField(max_length = 100)
    slug = models.SlugField()


    def __str__(self):

        return self.name

class Product(models.Model):

    name = models.CharField(max_length= 100)
    slug = models.SlugField()
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    image= models.ImageField(upload_to = 'uploads/')
    price= models.DecimalField(max_digits=10, decimal_places=2)



    def __str__(self):

        return self.name



