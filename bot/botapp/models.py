from django.db import models


class lettermaking(models.Model):
    Header = models.CharField(max_length=100)
    Body = models.TextField()
    Footer = models.CharField(max_length=100)
    CompanyName = models.CharField(max_length=100, blank=True, null=True)
    CompanyAddress = models.TextField(blank=True, null=True)
    CompanyPhone = models.CharField(max_length=20, blank=True, null=True)
    CompanyEmail = models.EmailField(blank=True, null=True)

class letterHistory(models.Model):
   fromNumber = models.CharField(max_length=100)
   pdfFile = models.CharField(max_length=100)
   date = models.DateTimeField(auto_now_add=True)
   
class currentProgress(models.Model):
   fromNumber = models.CharField(max_length=100)
   progress = models.CharField(max_length=100,default="Header")
   letterItems = models.ManyToManyField(lettermaking,blank=True)
   def __str__(self):
       return self.fromNumber