from django.db import models

# Create your models here.

class Avtosalon(models.Model):
    title = models.CharField(max_length=100)
    context = models.TextField()
    email =models.EmailField()
    phone = models.CharField()
    address = models.CharField(120)
    image = models.ImageField(upload_to='images/',blank=True, null=True, default='default/image.png')

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=40)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.TimeField(auto_now=True)
    context = models.TextField()
    brand_salon = models.ForeignKey(Avtosalon,on_delete=models.CASCADE,default=16)

    def __str__(self):
        return self.title


class Cars(models.Model):
    salon = models.ForeignKey(Avtosalon,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE)
    model = models.CharField()
    price = models.DecimalField(max_digits=12,decimal_places=2)
    year = models.PositiveIntegerField()
    color = models.CharField(max_length=30)
    
    def __str__(self):
        return self.model
