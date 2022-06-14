from django.db import models

# Create your models here.
class package(models.Model):
    package_id= models.IntegerField()
    package_name= models.CharField(max_length=200)
    price= models.FloatField()
    type= models.CharField(max_length=100)

class guide(models.Model):
    guide_id= models.IntegerField()
    guide_name= models.CharField(max_length=200)
    experience= models.IntegerField()
    type= models.CharField(max_length=100)
    contact_no= models.CharField(max_length=200)
    no_of_routes= models.IntegerField()
    review= models.CharField(max_length=500)

class agency(models.Model):
    agency_id= models.IntegerField()
    agency_name= models.CharField(max_length=200)
    location= models.CharField(max_length=200)
    package= models.ForeignKey(package, on_delete=models.CASCADE)
    class Meta:
        verbose_name_plural = "Agencies"

class booking(models.Model):
    booking_id= models.IntegerField()
    destination= models.CharField(max_length=200)
    ticket_type= models.CharField(max_length=200)
    #user= models.ForeignKey()
    guide= models.ForeignKey(guide, on_delete=models.CASCADE)
    package= models.ForeignKey(package, on_delete=models.CASCADE)




