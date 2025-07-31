from django.db import models

# Abstract Base Class for common fields
class Avtos(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True)  # Changed to DateTimeField for consistency

    class Meta:
        abstract = True

# Model for Avtosalon inheriting from Avtos
class Avtosalon(Avtos):
    title = models.CharField(max_length=100)
    context = models.TextField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)  # Specify max_length for CharField
    address = models.CharField(max_length=120)
    image = models.ImageField(upload_to='images/', blank=True, null=True, default='default/image.png')

    def __str__(self):
        return self.title

# Model for Brand inheriting from Avtos
class Brand(Avtos):
    title = models.CharField(max_length=40)
    context = models.TextField()
    brand_salon = models.ForeignKey(Avtosalon, on_delete=models.CASCADE, default=16)

    def __str__(self):
        return self.title

# Model for Cars inheriting from Avtos
class Cars(Avtos):
    salon = models.ForeignKey(Avtosalon, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)  # Specify max_length for CharField
    price = models.DecimalField(max_digits=12, decimal_places=2)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=30)

    def __str__(self):
        return self.model