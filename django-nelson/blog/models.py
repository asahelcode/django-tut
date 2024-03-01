from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
  class Staus(models.TextChoices):
    DRAFT = "drf", "Draft"
    PUBLISHED = "pud", "Published"
    Trash = "trs", "Trash"

  title = models.CharField(max_length=100)
  body = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  country = models.CharField(max_length=30, default="")
  status = models.CharField(max_length=3, choices=Staus.choices, default=Staus.DRAFT)

  def __str__(self):
    return self.title