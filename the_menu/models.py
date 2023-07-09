from django.db import models

class Member(models.Model):
  menu_item = models.CharField(max_length=255)
  price = models.CharField(max_length=255)
  describe = models.CharField(max_length=255)