from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
    ('M','MOBILE'),
    ('L','LAPTOP'),
    ('TW','Top wear'),
    ('BW','Bottom wear'),
)

class BrandCategory(models.Model):
    title = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    desc = models.TextField()
    slug = models.SlugField(default='')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2, default='')
    image = models.ImageField(upload_to='img')

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(BrandCategory,on_delete=models.CASCADE)
    slug = models.SlugField(default='')
    name = models.CharField(max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='productimg')


    def __str__(self):
        return self.name




