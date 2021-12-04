from django.db import models

# Create your models here.
class diet():
    age=models.IntegerField()
    blood = models.CharField(max_length=10)
    weight = models.IntegerField()
    height = models.CharField(max_length=10)
    foodtype = models.CharField(max_length=15)
    diet = models.TextField(max_length=1500)
    nutrient = models.TextField(max_length=1500)
    disease = models.TextField(max_length=1500)
    cuisines = models.TextField(max_length=1500)
    # image=models.ImageField(upload_to='website/images',default=r"C:\Users\MMG\Desktop\NBMRS\minor\media\website\images\avtar.png")
    second_time = models.BooleanField(default="False")
