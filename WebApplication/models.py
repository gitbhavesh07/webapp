from django.db import models
from django.contrib.auth.models import User

class userboard(models.Model):

 User_id = models.IntegerField()
 Month = models.CharField(max_length=30)
 Bp_Values = models.IntegerField()
 User_name = models.CharField(max_length=30)
 Hospital = models.CharField(max_length=30)
 
class graphinput(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  Month = models.CharField(max_length=30)
  Value1 = models.IntegerField(null=True,blank=True)
  Value2 = models.IntegerField()

  class Meta:
      db_table="WebApplication_graphinput"

class uploadfile(models.Model):
  Name = models.CharField(max_length=30)
  Pdf = models.FileField(upload_to='uploadmyfile/pdfs/')

  def __str__(self):
        return self.Name

  def delete(self, *args, **kwargs):
        self.Pdf.delete()
        super().delete(*args, **kwargs)