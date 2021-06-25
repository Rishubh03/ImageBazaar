from django.db import models

# Create your models here.

# Create categories model

class Category(models.Model):
  title=models.CharField(max_length=255)
  description=models.TextField()

  def __str__(self): 
      return self.title

# Create Image Model
class Images(models.Model):
  title=models.CharField(max_length=255)
  description=models.TextField()
  image=models.ImageField(upload_to='images')
  added_date=models.DateTimeField()
  cat=models.ForeignKey(Category, on_delete=models.CASCADE)

  def __str__(self):
    return self.title


