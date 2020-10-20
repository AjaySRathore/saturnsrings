from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Ringer(models.Model):
    """Creates Instance of Ringer. Ringers connects to django
       User via ForeignKey.

       Instance Fields
       user -- Instance of User Model.
       bio -- String Input with 500 char limit
    """
    #User cannot be deleted if Ringer exists.
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    bio = models.CharField(max_length=500,blank=True,
                verbose_name="Bio")

    def __str__(self):
        """Return username of Ringer"""
        return self.user.username

class Education(models.Model):
    """Creates Instance for Ringer Education.

       Instance Fields
       ringer -- Instance of Ringer model
       title -- title of Education with 100 char limit
       description -- description of education with 200 char limit
    """
    #Education record will be deleted with Ringer record delete action.
    ringer = models.ForeignKey(Ringer,on_delete=models.CASCADE,
                verbose_name="Ringer")
    title = models.CharField(max_length=100, verbose_name="Title")
    description = models.CharField(max_length=200,verbose_name="Descripiton",
                blank=True)

    def __str__(self):
        return self.title

class PastJob(models.Model):
    """Creates Instance for Ringer PastJob.

       Instance Fields
       ringer -- Instance of Ringer model
       position -- position name 100 char limit
       company -- company of PastJob with 100 char limit
       description -- description of PastJob with 500 char limit
    """
    #PastJob record will be deleted with Ringer record delete action.
    ringer = models.ForeignKey(Ringer,on_delete=models.CASCADE,
                verbose_name="Ringer")
    position = models.CharField(max_length=100, verbose_name="Position")
    company = models.CharField(max_length=100, verbose_name="Company")
    description = models.CharField(max_length=500,verbose_name="Descripiton",
                blank=True)

    def __str__(self):
        return self.position

class Certification(models.Model):
    """Creates Instance for Ringer Certification.

       Instance Fields
       ringer -- Instance of Ringer model
       title -- title with 100 char limit
       authority -- Name of authority Issuing certificate with 150 char limit
       description -- description of Certification with 250 char limit
    """
    #Certification record will be deleted with Ringer record delete action.
    ringer = models.ForeignKey(Ringer,on_delete=models.CASCADE,
                verbose_name="Ringer")
    title = models.CharField(max_length=100, verbose_name="title")
    authority = models.CharField(max_length=150, verbose_name="Issuing Authority")
    description = models.CharField(max_length=250,verbose_name="Descripiton",
                blank=True)

    def __str__(self):
        return self.position
