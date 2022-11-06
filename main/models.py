from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    STATUS = (
        (1, 'admin'),  # admin
        (2, 'users'),  # user
    )
    type = models.IntegerField(choices=STATUS, default=2)
    image = models.ImageField(upload_to='user/', null=True, blank=True)
    phone = models.CharField(max_length=225, null=True, blank=True)

class Information(models.Model):
    company_name = models.CharField(max_length=255)
    logo = models.ImageField(upload_to='informations/')
    description = models.TextField()
    googleplay = models.CharField(max_length=255)
    appstore = models.CharField(max_length=255)


class AdImage(models.Model):
    photo = models.ImageField(upload_to='image/')


class Category(models.Model):
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='category/')

class Distirc(models.Model):
    name = models.CharField(max_length=244)

class Region(models.Model):
    name = models.CharField(max_length=255)
    distirc = models.ManyToManyField(Distirc)

class Subcategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Ads(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    category = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    photo = models.ManyToManyField(AdImage)
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=100, decimal_places=2)
    status = models.IntegerField(choices=(
        (1, 'in admin'),
        (2, 'accepted'),
        (3, 'rejected'),
        (4, 'sold'),
    ), default=1)
    is_top = models.BooleanField(default=False)
    is_recommended = models.BooleanField(default=True)
    
class Helps_q(models.Model):
    question = models.CharField(max_length=244)

class Helps_a(models.Model):
    question = models.ForeignKey(Helps_q, on_delete=models.PROTECT)
    answer = models.TextField()


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=400)

class Wishlist(models.Model):
    ip = models.TextField()
    ads = models.ForeignKey(Ads, on_delete=models.CASCADE)
