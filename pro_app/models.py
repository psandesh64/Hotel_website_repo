from django.db import models
from  embed_video.fields  import  EmbedVideoField

# Create your models here.
class GetInTouch(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email =  models.EmailField(max_length=50)
    choose_option = models.CharField(max_length=50)
    phone = models.CharField(max_length=10)
    text_area = models.TextField()
    
class Category(models.Model):
    name = models.CharField(max_length=20,
                                choices=(('Buff','Buff'),('Chicken','Chicken'),('Vegetarian','Veg'))
                                )
    def __str__(self):
        return self.name
    
class Food_Items(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='categori')
    price = models.IntegerField()
    food_image = models.ImageField(upload_to='myMedia')

class Customer(models.Model):
    name = models.CharField(max_length=50)
    customer_image = models.ImageField(upload_to='myMedia')
    comment = models.TextField()

class Business_staff(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    b_staff_image = models.ImageField(upload_to='myMedia')
    comment = models.TextField()

class Team_staff(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    team_staff_image = models.ImageField(upload_to='myMedia')

class Videos(models.Model):
    name = models.CharField(max_length=50)
    video = EmbedVideoField()  # same like models.URLField()